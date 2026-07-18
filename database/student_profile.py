from utils.types import ResponseLength, StudentLevel, StudentProfile


class StudentProfileService:
    """يوفّر ملف الطالب. اليوم في الذاكرة؛ لاحقًا قاعدة بيانات فعلية."""

    def __init__(self):
        self._profiles: dict[int, StudentProfile] = {}

    def get_profile(self, user_id: int) -> StudentProfile:
        profile = self._profiles.get(user_id)
        if profile is None:
            profile = StudentProfile(
                user_id=user_id,
                level=StudentLevel.INTERMEDIATE,
                preferred_length=ResponseLength.NORMAL,
            )
            self._profiles[user_id] = profile
        return profile

    def save_profile(self, profile: StudentProfile) -> None:
        self._profiles[profile.user_id] = profile