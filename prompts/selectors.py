from utils.types import Audience, ResponseGoal, TeachingMode


class TeachingModeSelector:
    """اختيار وضع التدريس. قابل للاستبدال لاحقًا بأزرار تيليجرام أو مصنّف."""

    QUICK_WORDS = ("بسرعة", "بسرعه", "سريع", "باختصار", "اختصر", "مختصر", "مختصره", "quick")
    EXAM_WORDS = ("اختبار", "ميد", "فاينل", "مراجعة")
    DIRECT_WORDS = ("حل فقط", "الحل مباشر", "اعطني الحل", "أعطني الحل")
    GUIDED_WORDS = ("فهمني", "افهم", "أفهم", "وضح", "وضّح", "ليش", "لماذا", "كيف")
        
    @classmethod
    def select(cls, message: str) -> TeachingMode:
        text = message.lower()
        if any(w in text for w in cls.QUICK_WORDS):
            return TeachingMode.QUICK
        if any(w in text for w in cls.EXAM_WORDS):
            return TeachingMode.EXAM
        if any(w in text for w in cls.DIRECT_WORDS):
            return TeachingMode.DIRECT
        if any(w in text for w in cls.GUIDED_WORDS):
            return TeachingMode.GUIDED
        return TeachingMode.EXPLAIN


class ResponseGoalSelector:
    """اختيار هدف الرد بناءً على الوضع والرسالة."""

    HINT_WORDS = ("تلميح", "هنت", "hint")

    @classmethod
    def select(cls, mode: TeachingMode, message: str) -> ResponseGoal:
        text = message.lower()
        if any(w in text for w in cls.HINT_WORDS):
            return ResponseGoal.HINT
        if mode == TeachingMode.EXAM:
            return ResponseGoal.REVIEW
        if mode == TeachingMode.DIRECT:
            return ResponseGoal.SOLVE
        return ResponseGoal.TEACH


class AudienceSelector:
    @staticmethod
    def select(mode: TeachingMode) -> Audience:
        return Audience.EXAM if mode == TeachingMode.EXAM else Audience.STUDENT