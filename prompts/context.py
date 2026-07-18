from dataclasses import dataclass
from enum import Enum


class SourceType(str, Enum):
    MATCHED_SOLUTION = "matched_solution"
    SIMILAR_TECHNIQUE = "similar_technique"
    CONCEPTUAL = "conceptual"


@dataclass(frozen=True)
class StudentProfile:
    student_id: int
    level: str = "intermediate"
    response_length: str = "normal"
    audience: str = "student"


@dataclass(frozen=True)
class PromptContext:
    question: str
    context_text: str
    source_type: SourceType
    teaching_mode: str
    response_goal: str
    student_profile: StudentProfile
