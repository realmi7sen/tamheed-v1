import time
from dataclasses import dataclass, field


DAILY_QUESTION_LIMIT = 30
COOLDOWN_SECONDS = 10


@dataclass
class _UserUsage:
    day: int = 0
    count: int = 0
    last_ts: float = field(default=0.0)


class RateLimiter:
    """حد يومي + مهلة بين الأسئلة لكل مستخدم — حماية تكلفة الـ API.

    في الذاكرة حاليًا؛ عند الانتقال لقاعدة بيانات انقل العدادات لها
    حتى لا تُصفَّر عند إعادة تشغيل الخادم.
    """

    def __init__(
        self,
        daily_limit: int = DAILY_QUESTION_LIMIT,
        cooldown_seconds: int = COOLDOWN_SECONDS,
    ):
        self._daily_limit = daily_limit
        self._cooldown = cooldown_seconds
        self._usage: dict[int, _UserUsage] = {}

    def check(self, user_id: int) -> str | None:
        """يرجع None إذا مسموح، أو رسالة رفض جاهزة للإرسال."""
        now = time.time()
        today = int(now // 86400)
        usage = self._usage.setdefault(user_id, _UserUsage(day=today))

        if usage.day != today:
            usage.day = today
            usage.count = 0

        if now - usage.last_ts < self._cooldown:
            return "لحظة يا بطل، خلّص السؤال اللي قبله أول 😅 جرّب بعد ثواني."
        if usage.count >= self._daily_limit:
            return (
                "وصلت الحد اليومي للأسئلة (٣٠ سؤال). "
                "ارجع بكرة وكمّل — أو راجع الأسئلة اللي شرحناها اليوم 📚"
            )
        return None

    def record(self, user_id: int) -> None:
        usage = self._usage.setdefault(user_id, _UserUsage())
        usage.count += 1
        usage.last_ts = time.time()