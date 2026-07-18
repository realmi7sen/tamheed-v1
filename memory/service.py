class MemoryService:
    """Extension point for progress, misconceptions, and conversation memory."""

    def get_context(self, student_id: int) -> str:
        return ""
