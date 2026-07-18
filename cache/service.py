import hashlib


class ResponseCache:
    """طبقة كاش بسيطة في الذاكرة قبل استدعاء Claude."""

    def __init__(self, max_size: int = 512):
        self._store: dict[str, str] = {}
        self._max_size = max_size

    @staticmethod
    def make_key(system_prompt: str, user_prompt: str) -> str:
        raw = f"{system_prompt}\n---\n{user_prompt}".encode("utf-8")
        return hashlib.sha256(raw).hexdigest()

    def get(self, key: str) -> str | None:
        return self._store.get(key)

    def set(self, key: str, value: str) -> None:
        if len(self._store) >= self._max_size:
            self._store.pop(next(iter(self._store)))
        self._store[key] = value