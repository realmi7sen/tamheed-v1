class RetrievalError(Exception):
    """Knowledge retrieval failed."""


class DatabaseError(Exception):
    """Student-profile persistence failed."""


class LLMServiceError(Exception):
    """The language-model provider returned an error."""


class LLMTimeoutError(LLMServiceError):
    """The language-model provider timed out."""
