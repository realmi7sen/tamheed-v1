from utils.types import ResponseLength, StudentLevel, StudentProfile


BEGINNER_RATE = 0.35
ADVANCED_RATE = 0.15
MIN_SIGNALS = 8
WEAK_SCORE = 0.5


class StudentProfileService:
    """يبني ملف الطالب من إشارات التعلّم المخزّنة."""

    def __init__(self, db):
        self.db = db

    def get_profile(self, user_id: int) -> StudentProfile:
        signals = self.db.signals_recent(user_id, limit=20)

        level = StudentLevel.INTERMEDIATE
        weak_topics: list[str] = []

        if len(signals) >= MIN_SIGNALS:
            confused = sum(
                1 for s in signals
                if (s["retrieval_score"] or 0) < WEAK_SCORE
            )
            rate = confused / len(signals)

            if rate > BEGINNER_RATE:
                level = StudentLevel.BEGINNER
            elif rate < ADVANCED_RATE:
                level = StudentLevel.ADVANCED

            weak_topics = self._weak_topics(signals)

        return StudentProfile(
            user_id=user_id,
            level=level,
            preferred_length=ResponseLength.NORMAL,
            metadata={"weak_topics": weak_topics},
        )

    @staticmethod
    def _weak_topics(signals: list) -> list[str]:
        """مواضيع تبعها الطالب بسؤال متابعة — إشارة على عدم الفهم."""
        weak: dict[str, int] = {}
        # signals راجعة من الأحدث للأقدم
        for newer, older in zip(signals, signals[1:]):
            if (newer["retrieval_score"] or 0) < WEAK_SCORE:
                topic = older["topic"]
                if topic:
                    weak[topic] = weak.get(topic, 0) + 1
        return sorted(weak, key=weak.get, reverse=True)[:3]

    def save_profile(self, profile: StudentProfile) -> None:
        pass