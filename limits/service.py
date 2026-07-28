import time
import os
from database.db import TamheedDB
from datetime import datetime, timezone, timedelta

ADMIN_CHAT_ID = os.environ.get("ADMIN_CHAT_ID")
ADMIN_ID_INT = int(ADMIN_CHAT_ID) if ADMIN_CHAT_ID else None 

DAILY_QUESTION_LIMIT = 30
COOLDOWN_SECONDS = 10
CACHE_THRESHOLD_USERS = 40
CACHE_WINDOW_MINUTES = 5

REDUCE_DATE = datetime(2026, 9, 15, tzinfo=timezone.utc)  # set the real 2/3-term date
REDUCED_LIMIT = 15
class RateLimiter:
    """حد يومي + مهلة بين الأسئلة — SQLite."""

    def __init__(
        self,
        daily_limit: int = DAILY_QUESTION_LIMIT,
        cooldown_seconds: int = COOLDOWN_SECONDS,
        db_path: str | None = None,
    ):
        self._daily_limit = daily_limit
        self._cooldown = cooldown_seconds
        self.db = TamheedDB(db_path or os.environ.get("DB_PATH", "tamheed.db"))

    def check(self, user_id: int) -> str | None:
        """يرجع None إذا مسموح، أو رسالة رفض."""
        if ADMIN_ID_INT is not None and user_id == ADMIN_ID_INT:
            return None  # admin bypasses cooldown + daily limit entirely

        now = time.time()
        today = int(now // 86400)

        usage = self.db.usage_get(user_id, today)
        count = usage["count"]
        last_ts = usage["last_message_ts"]

        if now - last_ts < self._cooldown:
            return "لحظة يا بطل، خلّص السؤال اللي قبله أول 😅 جرّب بعد ثواني."

        active_limit = self._get_active_limit()
        if count >= active_limit:
            return (
                f"وصلت الحد اليومي للأسئلة ({active_limit} سؤال). "
                "ارجع بكرة وكمّل — أو راجع الأسئلة اللي شرحناها اليوم 📚"
            )
        return None
    
    def _get_active_limit(self) -> int:
        now_utc = datetime.now(timezone.utc)
        if now_utc >= REDUCE_DATE:
            return REDUCED_LIMIT
        return self._daily_limit

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