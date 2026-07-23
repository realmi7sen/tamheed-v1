from dataclasses import dataclass, field
from enum import Enum


class SourceType(str, Enum):
    """مصدر الدليل المستخدم في بناء الرد."""

    MATCHED_SOLUTION = "matched_solution"
    SIMILAR_TECHNIQUE = "similar_technique"
    CONCEPTUAL = "conceptual"


class TeachingMode(str, Enum):
    QUICK = "quick"
    EXAM = "exam"
    DIRECT = "direct"
    GUIDED = "guided"
    EXPLAIN = "explain"


class ResponseGoal(str, Enum):
    TEACH = "teach"
    SOLVE = "solve"
    REVIEW = "review"
    HINT = "hint"


class StudentLevel(str, Enum):
    BEGINNER = "beginner"
    INTERMEDIATE = "intermediate"
    ADVANCED = "advanced"


class ResponseLength(str, Enum):
    SHORT = "short"
    NORMAL = "normal"
    LONG = "long"


class Audience(str, Enum):
    STUDENT = "student"
    EXAM = "exam"


@dataclass
class StudentProfile:
    """ملف الطالب: يستبدل المتغيرات المنفصلة مثل student_level."""

    user_id: int
    level: StudentLevel = StudentLevel.INTERMEDIATE
    preferred_length: ResponseLength = ResponseLength.NORMAL
    metadata: dict = field(default_factory=dict)


@dataclass
class RetrievalResult:
    """ناتج طبقة الاسترجاع بعد تحديد نوع الدليل."""

    context_text: str
    source: SourceType
    score: float = 0.0
    technique_name: str = ""


@dataclass
class PromptContext:
    """كل ما يحتاجه بناء البرومبت في كائن واحد بدل تمرير نص يدوي."""

    user_message: str
    context_text: str
    source: SourceType
    teaching_mode: 'TeachingMode'
    response_goal: 'ResponseGoal'
    student_level: StudentLevel
    response_length: ResponseLength
    audience: 'Audience'
    technique_name: str = ""
    retrieval_score: float = 0.0
    technique_name: str = ""
    retrieval_score: float = 0.0
    weak_topics: list = field(default_factory=list)