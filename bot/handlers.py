from anthropic import AnthropicError
from telegram import Update
from telegram.ext import ContextTypes

from bot.greetings import GreetingHandler
from cache.service import ResponseCache
from database.student_profile import StudentProfileService
from formatter.response import ResponseFormatter
from limits.service import RateLimiter
from llm.client import TamheedLLMClient
from memory.service import MemoryService
from prompts.builder import build_system_prompt, build_user_prompt
from prompts.selectors import (
    AudienceSelector,
    ResponseGoalSelector,
    TeachingModeSelector,
)
from retrieval.knowledge import KnowledgeService
from services.display import DisplayService
from services.tools import ToolService
from utils.errors import DatabaseError, LLMTimeoutError, RetrievalError
from utils.types import PromptContext, ResponseLength, TeachingMode

import os
from datetime import datetime, timezone

from limits.service import RateLimiter, CACHE_THRESHOLD_USERS, CACHE_WINDOW_MINUTES

ADMIN_CHAT_ID = os.environ.get("ADMIN_CHAT_ID")
ADMIN_ID_INT = int(ADMIN_CHAT_ID) if ADMIN_CHAT_ID else None

DEBUG = os.environ.get("DEBUG") == "1"

MEMORY_WINDOW_SECONDS = 20*60
MEMORY_WINDOW_CHARS = 1000

# ===== ACCESS GATE =====
FREE_QUESTION_LIMIT = 5   # أسئلة مجانية مدى الحياة لأي شخص
# تاريخ انتهاء الاشتراك — آخر الترم. عدّلها للتاريخ الحقيقي.
SUBSCRIPTION_EXPIRES_AT = "2026-12-31 23:59:59"

SUBSCRIBE_MESSAGE = (
    "خلصت أسئلتك المجانية (٥ أسئلة) 🎓\n"
    "للاستمرار، اشترك واحصل على ٢٠ سؤال يومياً لبقية الترم.\n"
    "للاشتراك تواصل معنا، وبعد الدفع بيوصلك كود.\n"
    "فعّل الكود بالأمر:  /redeem الكود"
)

FOLLOWUP_ROOTS = (
    "كمل", "أكمل", "اكمل",
    "وضح", "وضّح",
    "فهم",
    "زياد", "أكثر", "اكثر",
    "بعده", "بعدها",
    "يعني",
    "ثاني", "اعد", "أعد",
    "كلم",
    "قصد",
    "فوق",
    "قبل",
    "نفس",
    "بسّط", "بسط",
    "كرر", "عيد",
    "مثال",
    "طيب", "طب",
)


def is_followup(text: str) -> bool:
    words = text.split()
    for word in words:
        clean = word.strip("؟?.,!:؛\"'()")
        for root in FOLLOWUP_ROOTS:
            if clean.startswith(root):
                return True
    return False


class TamheedMessageHandler:
    def __init__(
        self,
        knowledge_service: KnowledgeService,
        llm_client: TamheedLLMClient,
        profile_service: StudentProfileService,
        response_formatter: ResponseFormatter,
        memory_service: MemoryService,
        tool_service: ToolService,
        display_service: DisplayService,
        cache: ResponseCache,
        rate_limiter: RateLimiter,
    ):
        self.knowledge = knowledge_service
        self.llm = llm_client
        self.profiles = profile_service
        self.formatter = response_formatter
        self.memory = memory_service
        self.tools = tool_service
        self.display = display_service
        self.cache = cache
        self.limiter = rate_limiter
        self.db = rate_limiter.db

    async def _notify_admin(self, context: ContextTypes.DEFAULT_TYPE, error: Exception, kind: str) -> None:
        if not ADMIN_CHAT_ID:
            return
        try:
            await context.bot.send_message(
                chat_id=ADMIN_CHAT_ID,
                text=f"⚠️ {kind}:\n{error}",
            )
        except Exception:
            pass

    def _access_check(self, user_id: int) -> str | None:
        """
        بوابة الوصول — تقرر إذا يُسمح للطالب بسؤال قبل أي استدعاء لـ Claude.
        يرجع None إذا مسموح، أو رسالة رفض.
        - الأدمن: يمر دائماً.
        - المشترك: يمر (الحد اليومي ٢٠ يتكفّل به RateLimiter لاحقاً).
        - المجاني تحت ٥: يمر.
        - المجاني عند ٥: رسالة الاشتراك، بدون استدعاء المحرك.
        """
        if ADMIN_ID_INT is not None and user_id == ADMIN_ID_INT:
            return None
        if self.db.is_subscribed(user_id):
            return None
        if self.db.free_used_get(user_id) < FREE_QUESTION_LIMIT:
            return None
        return SUBSCRIBE_MESSAGE

    def _is_free_user(self, user_id: int) -> bool:
        """طالب مجاني = ليس أدمن وليس مشترك. يُستخدم لعدّ الأسئلة المجانية."""
        if ADMIN_ID_INT is not None and user_id == ADMIN_ID_INT:
            return False
        return not self.db.is_subscribed(user_id)

    async def redeem(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """أمر /redeem — تفعيل كود اشتراك."""
        user_id = update.effective_user.id
        parts = (update.message.text or "").split()

        if len(parts) < 2:
            await update.message.reply_text(
                "اكتب الكود بعد الأمر، مثال:\n/redeem TAMHEED-XXXX"
            )
            return

        code = parts[1].strip()
        result = self.db.redeem_code(code, user_id, SUBSCRIPTION_EXPIRES_AT)

        if result == "ok":
            await update.message.reply_text(
                "تم تفعيل اشتراكك ✅\n"
                "معك ٢٠ سؤال يومياً لبقية الترم. اسأل اللي تبي 📚"
            )
        elif result == "used":
            await update.message.reply_text(
                "هذا الكود مستخدم من قبل ❌ تأكد من الكود أو تواصل معنا."
            )
        else:  # not_found
            await update.message.reply_text(
                "الكود غير صحيح ❌ تأكد من كتابته صح."
            )

    async def handle(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        user_message = update.message.text

        if len(user_message) > MEMORY_WINDOW_CHARS:
           await update.message.reply_text(
                "رسالتك طويلة شوي 😅 اختصر سؤالك أو قسّمه لأجزاء، "
                "وأنا بساعدك ."
            )
           return

        if GreetingHandler.is_greeting(user_message):
            await GreetingHandler.reply(update)
            return

        user_id = update.effective_user.id

        # ===== بوابة الوصول: قبل أي استدعاء للمحرك =====
        access_denial = self._access_check(user_id)
        if access_denial:
            await update.message.reply_text(access_denial)
            return

        # الحد اليومي + المهلة (للمشتركين والأدمن)
        denial = self.limiter.check(user_id)
        if denial:
            await update.message.reply_text(denial)
            return

        await context.bot.send_chat_action(
            chat_id=update.effective_chat.id, action="typing"
        )

        recent_enough = (
              self.limiter.seconds_since_last(user_id)
              <= MEMORY_WINDOW_SECONDS
        )

        history = self.db.conversation_get_recent(
           user_id,
           limit=2,
        )

        use_memory = (
            recent_enough
            and len(history) >= 1
        )

        try:
            prompt_context = await self._build_prompt_context(
                user_id, user_message
            )
            reply = await self._generate(
                prompt_context, user_id=user_id, use_memory=use_memory
            )
        except RetrievalError as error:
            await update.message.reply_text("عذراً، صار خطأ في البحث عن الحل.")
            print(f"RetrievalError: {error}")
            await self._notify_admin(context, error, "RetrievalError")
            return
        except DatabaseError as error:
            await update.message.reply_text("عذراً، ما قدرت أوصل لملفك، جرّب بعد شوي.")
            print(f"DatabaseError: {error}")
            await self._notify_admin(context, error, "DatabaseError")
            return
        except LLMTimeoutError as error:
            await update.message.reply_text("المحرك تأخر بالرد، جرّب مرة ثانية.")
            print(f"LLMTimeoutError: {error}")
            await self._notify_admin(context, error, "LLMTimeoutError")
            return
        except AnthropicError as error:
            await update.message.reply_text("عذراً، حدث خطأ في التواصل مع المحرك.")
            print(f"AnthropicError: {error}")
            await self._notify_admin(context, error, "AnthropicError")
            return

        self.limiter.record(user_id)

        # عُدّ السؤال المجاني فقط بعد نجاح الرد (لا نحرق رصيد على خطأ)
        if self._is_free_user(user_id):
            self.db.free_used_increment(user_id)

        # سجّل السؤال للقياس — بعد نجاح الرد فقط، وبدون الأدمن
        if not (ADMIN_ID_INT is not None and user_id == ADMIN_ID_INT):
            self.db.log_question(user_id, user_message)

        

        self.db.signal_add(
            user_id=user_id,
            topic=prompt_context.technique_name or "",
            teaching_mode=prompt_context.teaching_mode.value,
            retrieval_score=prompt_context.retrieval_score,
            was_followup=is_followup(user_message),
        )
        self.db.student_touch(
            user_id,
            update.effective_user.username or "",
            update.effective_user.first_name or "",
        )

        self.db.conversation_add(user_id, "user", user_message)
        self.db.conversation_add(user_id, "assistant", reply)
        self.db.conversation_clear_old(user_id, keep_count=50)

        for chunk in self.formatter.split(self.display.prepare(reply)):
            await update.message.reply_text(chunk)

    async def clear_memory(
        self, update: Update, context: ContextTypes.DEFAULT_TYPE
    ) -> None:
        user_id = update.effective_user.id
        self.db.conversation_clear_old(user_id, keep_count=0)
        await update.message.reply_text("تمام، بدينا من جديد ✨ اسأل اللي تبي.")

    async def handle_media(
        self, update: Update, context: ContextTypes.DEFAULT_TYPE
    ) -> None:
        msg = update.message
        media_type = (
            "voice" if msg.voice
            else "photo" if msg.photo
            else "document" if msg.document
            else "video" if msg.video
            else "other"
        )
        try:
            self.db.log_media(update.effective_user.id, media_type)
        except Exception:
            pass
        await msg.reply_text("حالياً أستقبل أسئلة نصية بس 🙏 اكتب سؤالك وأنا حاضر")

    async def _build_prompt_context(
        self, user_id: int, user_message: str
    ) -> PromptContext:
        profile = self.profiles.get_profile(user_id)
        retrieval = await self.knowledge.search(user_message)
        is_followup_q = len(user_message) <= 15 and not any(c in user_message for c in "0123456789x∫√")
        previous_answer = ""

        if is_followup_q:
            context_text = ""
            previous_answer = self.db.conversation_last_assistant(user_id) or ""
        else:
            context_text = self.formatter.format_context(retrieval.context_text)


        teaching_mode = TeachingModeSelector.select(user_message)
        response_goal = ResponseGoalSelector.select(teaching_mode, user_message)
        audience = AudienceSelector.select(teaching_mode)

        response_length = profile.preferred_length
        if teaching_mode == TeachingMode.QUICK:
            response_length = ResponseLength.SHORT

        return PromptContext(
            user_message=user_message,
            context_text=context_text,
            source=retrieval.source,
            teaching_mode=teaching_mode,
            response_goal=response_goal,
            student_level=profile.level,
            response_length=response_length,
            audience=audience,
            technique_name=retrieval.technique_name,
            retrieval_score=retrieval.score,
            weak_topics=profile.metadata.get("weak_topics", []),
            is_followup=is_followup_q,
            previous_answer=previous_answer,
        )


    async def _generate(
        self, ctx: PromptContext, user_id: int, use_memory: bool
    ) -> str:
        base_prompt, variable_prompt = build_system_prompt(ctx)
        user_prompt = build_user_prompt(ctx)

        history = []
        if use_memory:
            prev = self.db.conversation_get_recent(user_id, limit=1)
            if prev:
                questions = "\n".join(f"- {m['content']}" for m in prev)
                user_prompt = (
                    f"أسئلة الطالب السابقة (للسياق فقط، لا تجب عليها):\n{questions}\n\n"
                    f"{user_prompt}"
                )

        if not use_memory:
         cache_key = self.cache.make_key(base_prompt + variable_prompt, user_prompt)
         cached = self.cache.get(cache_key)
         if cached is not None:
            return cached

        enable_cache = True


        reply = await self.llm.generate(
            base_prompt=base_prompt,
            variable_prompt=variable_prompt,
            user_prompt=user_prompt,
            response_length=ctx.response_length,
            history=history,
            enable_cache=enable_cache,
        )

        if not use_memory:
            self.cache.set(cache_key, reply)
        return reply
    
    