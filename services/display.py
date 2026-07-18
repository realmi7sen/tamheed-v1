from formatter.telegram_clean import clean_markdown


class DisplayService:
    """يهيّئ الانتقال لاحقًا إلى Telegram Mini App، وينظّف Markdown قبل الإرسال."""

    def prepare(self, reply: str) -> str:
        return clean_markdown(reply)


TelegramFormatter = DisplayService