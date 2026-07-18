class DisplayService:
    """يهيّئ الانتقال لاحقًا إلى Telegram Mini App."""

    def prepare(self, reply: str) -> str:
        return reply


TelegramFormatter = DisplayService