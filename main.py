from pathlib import Path
import os
import sys

from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

from bot.handlers import TamheedMessageHandler
from bot.greetings import GreetingHandler
from cache.service import ResponseCache
from database.student_profile import StudentProfileService
from formatter.response import ResponseFormatter
from llm.client import TamheedLLMClient
from memory.service import MemoryService
from retrieval.knowledge import KnowledgeService
from services.display import DisplayService
from services.tools import ToolService


PROJECT_DIR = Path(__file__).resolve().parent
load_dotenv(PROJECT_DIR / ".env")
sys.stdout.reconfigure(encoding="utf-8")


def create_application():
    telegram_token = os.environ.get("TELEGRAM_TOKEN")
    if not telegram_token:
        raise RuntimeError("TELEGRAM_TOKEN is missing. Check the .env file.")

    project_root = PROJECT_DIR.parents[0]
    knowledge_service = KnowledgeService(
        persist_dir=project_root / "Knowledge_Base" / "Math106_index"
    )
    response_formatter = ResponseFormatter()
    handler = TamheedMessageHandler(
        knowledge_service=knowledge_service,
        llm_client=TamheedLLMClient(),
        profile_service=StudentProfileService(),
        response_formatter=response_formatter,
        memory_service=MemoryService(),
        tool_service=ToolService(),
        display_service=DisplayService(),
        cache=ResponseCache(),
    )

    app = ApplicationBuilder().token(telegram_token).build()
    app.add_handler(CommandHandler("start", GreetingHandler.start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handler.handle))
    return app


if __name__ == "__main__":
    try:
        app = create_application()
        print("Tamheed bot is running...")
        app.run_polling()
    except RuntimeError as error:
        print(f"CRITICAL ERROR: {error}")
        sys.exit(1)
