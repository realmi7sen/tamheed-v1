from telegram import Update
from telegram.ext import ContextTypes


class GreetingHandler:
    """اكتشاف التحية والرد على أمر /start."""

    GREETINGS = (
        "السلام", "هلا", "مرحبا", "صباح", "مساء", "اهلا",
        "كيف حالك", "hi", "hello", "hey", "مرحباً",
    )
    MAX_LEN = 50

    @classmethod
    def is_greeting(cls, message: str) -> bool:
        text = message.lower()
        return len(message) < cls.MAX_LEN and any(g in text for g in cls.GREETINGS)

    @staticmethod
    async def reply(update: Update) -> None:
        await update.message.reply_text(
            "هلا! 👋\nاسألني عن أي موضوع من ريض ١٠٦ وأساعدك."
        )

    @staticmethod
    async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        await update.message.reply_text(
            "هلا! 👋\nأنا تمهيد، اسألني أي سؤال عن ريض 106."
        )