from pathlib import Path
import os
import sys
from admin import AdminHandler
from dotenv import load_dotenv

PROJECT_DIR = Path(__file__).resolve().parent
load_dotenv(PROJECT_DIR / ".env")
from prompts.base import BASE_PROMPT, check_cacheable, _MIN_CACHEABLE


from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

from bot.handlers import TamheedMessageHandler
from bot.greetings import GreetingHandler
from cache.service import ResponseCache
from database.student_profile import StudentProfileService
from formatter.response import ResponseFormatter
from limits.service import RateLimiter
from llm.client import TamheedLLMClient
from memory.service import MemoryService
from retrieval.knowledge import KnowledgeService
from services.display import DisplayService
from services.tools import ToolService

sys.stdout.reconfigure(encoding="utf-8")


def create_application():
    telegram_token = os.environ.get("TELEGRAM_TOKEN")
    if not telegram_token:
        raise RuntimeError("TELEGRAM_TOKEN is missing. Check the .env file.")

    ADMIN_CHAT_ID = os.environ.get("ADMIN_CHAT_ID")

    project_root = PROJECT_DIR
    knowledge_service = KnowledgeService(
        persist_dir=project_root / "Knowledge_Base" / "Math106_index",
        top_k=2,
    )
    response_formatter = ResponseFormatter()
    rate_limiter = RateLimiter()
    admin_handler = AdminHandler(str(rate_limiter.db.db_path))
    handler = TamheedMessageHandler(
        knowledge_service=knowledge_service,
        llm_client=TamheedLLMClient(),
        profile_service=StudentProfileService(rate_limiter.db),
        response_formatter=response_formatter,
        memory_service=MemoryService(),
        tool_service=ToolService(),
        display_service=DisplayService(),
        cache=ResponseCache(),
        rate_limiter=rate_limiter,
    )

    async def post_init(application):
        n, ok = check_cacheable()
        if n is None:
            return
        print(f"[BOOT] BASE_PROMPT = {n} tokens (cache floor {_MIN_CACHEABLE})")
        if ok:
            return
        msg = (
            f"⚠️ BASE_PROMPT dropped to {n} tokens — below the "
            f"{_MIN_CACHEABLE} cache floor. Prompt caching is OFF. "
            f"Cost per question is roughly 2.5x. Revert the last edit to "
            f"prompts/base.py or pad it back above {_MIN_CACHEABLE + _SAFETY}."
        )
        print(msg)
        if ADMIN_CHAT_ID:
            try:
                await application.bot.send_message(chat_id=ADMIN_CHAT_ID, text=msg)
            except Exception:
                pass

    #commands wither it's by the admin or the user
    app = ApplicationBuilder().token(telegram_token).post_init(post_init).build()
    app.add_handler(CommandHandler("start", GreetingHandler.start))
    app.add_handler(CommandHandler("new", handler.clear_memory))
    app.add_handler(CommandHandler("stats", admin_handler.stats))
    app.add_handler(CommandHandler("dashboard", admin_handler.dashboard))
    app.add_handler(CommandHandler("backup", admin_handler.backup))
    app.add_handler(CommandHandler("redeem", handler.redeem))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handler.handle))
    app.add_handler(MessageHandler(filters.VOICE | filters.PHOTO | filters.Document.ALL | filters.VIDEO, handler.handle_media))

    async def error_handler(update, context):
        print(f"Error: {context.error}")
        if ADMIN_CHAT_ID:
            try:
                await context.bot.send_message(
                    chat_id=ADMIN_CHAT_ID,
                    text=f"⚠️ خطأ في البوت:\n{context.error}",
                )
            except Exception:
                pass
        if update and hasattr(update, "message") and update.message:
            try:
                await update.message.reply_text(
                    "صار خطأ مؤقت، جرب مرة ثانية بعد شوي 🙏"
                )
            except Exception:
                pass

    app.add_error_handler(error_handler)
    return app


if __name__ == "__main__":
    try:
        app = create_application()
        print("Tamheed bot is running...")
        app.run_polling()
    except RuntimeError as error:
        print(f"CRITICAL ERROR: {error}")
        sys.exit(1)