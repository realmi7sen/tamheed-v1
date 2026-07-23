import time
from database.db import TamheedDB


DAILY_QUESTION_LIMIT = 1000
COOLDOWN_SECONDS = 10
CACHE_THRESHOLD_USERS = 40
CACHE_WINDOW_MINUTES = 5


class RateLimiter:
    """حد يومي + مهلة بين الأسئلة — SQLite."""

    def __init__(
        self,
        daily_limit: int = DAILY_QUESTION_LIMIT,
        cooldown_seconds: int = COOLDOWN_SECONDS,
        db_path: str = "tamheed.db",
    ):
        self._daily_limit = daily_limit
        self._cooldown = cooldown_seconds
        self.db = TamheedDB(db_path)

    def check(self, user_id: int) -> str | None:
        """يرجع None إذا مسموح، أو رسالة رفض."""
        now = time.time()
        today = int(now // 86400)

        usage = self.db.usage_get(user_id, today)
        count = usage["count"]
        last_ts = usage["last_message_ts"]

        if now - last_ts < self._cooldown:
            return "لحظة يا بطل، خلّص السؤال اللي قبله أول 😅 جرّب بعد ثواني."
        if count >= self._daily_limit:
            return (
                "وصلت الحد اليومي للأسئلة (٣٠ سؤال). "
                "ارجع بكرة وكمّل — أو راجع الأسئلة اللي شرحناها اليوم 📚"
            )
        return None

    def record(self, user_id: int) -> None:
        now = time.time()
        today = int(now // 86400)
        self.db.usage_increment(user_id, today, now)

    def seconds_since_last(self, user_id: int) -> float:
        """كم ثانية مرت من آخر رسالة — للنافذة الزمنية للذاكرة."""
        now = time.time()
        today = int(now // 86400)
        usage = self.db.usage_get(user_id, today)
        last_ts = usage["last_message_ts"]
        if last_ts == 0:
            return float("inf")
        return now - last_ts