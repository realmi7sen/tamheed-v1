TELEGRAM_MAX_CHARS = 4096


class ResponseFormatter:
    """مسؤول عن تنسيق سياق الإدخال وتنسيق/تقسيم الردود."""

    def format_context(self, context_text: str) -> str:
        return context_text.strip()

    def format_reply(self, reply: str) -> str:
        return reply.strip()

    def split(self, reply: str, limit: int = TELEGRAM_MAX_CHARS) -> list[str]:
        text = self.format_reply(reply)
        if len(text) <= limit:
            return [text]

        chunks: list[str] = []
        current = ""
        for paragraph in text.split("\n\n"):
            candidate = f"{current}\n\n{paragraph}" if current else paragraph
            if len(candidate) <= limit:
                current = candidate
                continue
            if current:
                chunks.append(current)
            if len(paragraph) <= limit:
                current = paragraph
            else:
                for i in range(0, len(paragraph), limit):
                    chunks.append(paragraph[i : i + limit])
                current = ""
        if current:
            chunks.append(current)
        return chunks