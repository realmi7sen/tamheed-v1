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


MEMORY_WINDOW_SECONDS = 20*60
MEMORY_WINDOW_CHARS = 1000

FOLLOWUP_ROOTS = (
    "كمل", "أكمل", "اكمل",
    "وضح", "وضّح",
    "فهم",
    "ليش", "لماذا",
    "زياد", "أكثر", "اكثر",
    "بعده", "بعدها",
    "يعني",
    "ثاني", "اعد", "أعد",
    "كلم",                      # تتكلم / كلامك / تكلمت
    "قصد",                      # قصدك / وش تقصد
    "فوق",                      # اللي فوق / الكلام فوق
    "قبل",                      # اللي قبل / قبل شوي
    "هذا", "هذي", "ذا",         # وش هذا / هذي كيف
    "نفس",                      # نفس الشي / نفس المسألة
    "بسّط", "بسط",              # بسّطها
    "كرر", "عيد",               # كررها / عيدها
    "مثال",                     # أعطني مثال (على السابق)
    "طيب", "طب",                # طيب وبعد
    "وش",                       # وش يعني / وش هذا — متابعة قصيرة شائعة
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

        denial = self.limiter.check(update.effective_user.id)
        if denial:
            await update.message.reply_text(denial)
            return

        await context.bot.send_chat_action(
            chat_id=update.effective_chat.id, action="typing"
        )

        user_id = update.effective_user.id
        use_memory = is_followup(user_message) and (
            self.limiter.seconds_since_last(user_id) <= MEMORY_WINDOW_SECONDS
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
            return
        except DatabaseError as error:
            await update.message.reply_text("عذراً، ما قدرت أوصل لملفك، جرّب بعد شوي.")
            print(f"DatabaseError: {error}")
            return
        except LLMTimeoutError as error:
            await update.message.reply_text("المحرك تأخر بالرد، جرّب مرة ثانية.")
            print(f"LLMTimeoutError: {error}")
            return
        except AnthropicError as error:
            await update.message.reply_text("عذراً، حدث خطأ في التواصل مع المحرك.")
            print(f"AnthropicError: {error}")
            return

        self.limiter.record(user_id)

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

    async def _build_prompt_context(
        self, user_id: int, user_message: str
    ) -> PromptContext:
        profile = self.profiles.get_profile(user_id)
        retrieval = await self.knowledge.search(user_message)
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
        )

    async def _generate(
        self, ctx: PromptContext, user_id: int, use_memory: bool
    ) -> str:
        system_prompt = build_system_prompt(ctx)
        user_prompt = build_user_prompt(ctx)

        history = []
        if use_memory:
            history = self.db.conversation_get_recent(user_id, limit=6)

        if not use_memory:
            cache_key = self.cache.make_key(system_prompt, user_prompt)
            cached = self.cache.get(cache_key)
            if cached is not None:
                return cached

        reply = await self.llm.generate(
            system_prompt=system_prompt,
            user_prompt=user_prompt,
            response_length=ctx.response_length,
            history=history,
        )

        if not use_memory:
            self.cache.set(cache_key, reply)
        return reply