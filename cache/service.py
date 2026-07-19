import hashlib
import re
from database.db import TamheedDB


class ResponseCache:
    """كاش SQLite مع تنظيف النص — الأسئلة القريبة = نفس الجواب."""

    def __init__(self, db_path: str = "tamheed.db"):
        self.db = TamheedDB(db_path)

    @staticmethod
    def normalize_text(text: str) -> str:
        """تنظيف النص — احذف مسافات زايدة وحول لحروف صغيرة."""
        text = " ".join(text.split())
        text = text.lower()
        text = text.strip()
        return text

    @staticmethod
    def make_key(system_prompt: str, user_prompt: str) -> str:
        """صنع مفتاح — نظّف السؤال بس، وخلّي system_prompt كما هو."""
        cleaned_user = ResponseCache.normalize_text(user_prompt)
        raw = f"{system_prompt}\n---\n{cleaned_user}".encode("utf-8")
        return hashlib.sha256(raw).hexdigest()

    def get(self, key: str) -> str | None:
        """ابحث في SQLite عن المفتاح."""
        return self.db.cache_get(key)

    def set(self, key: str, value: str) -> None:
        """خزّن الرد في SQLite."""
        self.db.cache_set(key, value)