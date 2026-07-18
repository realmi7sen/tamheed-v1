from pathlib import Path

from llama_index.core import Settings, StorageContext, load_index_from_storage
from llama_index.embeddings.cohere import CohereEmbedding

from utils.errors import RetrievalError
from utils.types import RetrievalResult, SourceType


# عتبات القرار — معزولة كي يسهل ضبطها لاحقًا.
MATCH_THRESHOLD = 0.78
STRONG_MATCH_THRESHOLD = 0.90


class KnowledgeService:
    """يغلّف بناء الفهرس والاسترجاع وقرار نوع الدليل."""

    def __init__(self, persist_dir: Path, top_k: int = 1):
        Settings.embed_model = CohereEmbedding(
            api_key=_require_cohere_key(),
            model_name="embed-multilingual-v3.0",
            input_type="search_query",
        )
        storage_context = StorageContext.from_defaults(persist_dir=str(persist_dir))
        index = load_index_from_storage(storage_context)
        self._retriever = index.as_retriever(similarity_top_k=top_k)

    async def search(self, query: str) -> RetrievalResult:
        try:
            nodes = await self._retriever.aretrieve(query)
        except Exception as error:
            raise RetrievalError(str(error)) from error

        top = nodes[0] if nodes else None
        score = float(getattr(top, "score", 0) or 0) if top else 0.0

        if not top or score < MATCH_THRESHOLD:
            return RetrievalResult(
                context_text="لا يوجد ملف معتمد مطابق لهذا السؤال في بنك الحلول.",
                source=SourceType.CONCEPTUAL,
                score=score,
            )

        doc_type = top.metadata.get("doc_type", "")
        coverage_verified = top.metadata.get("coverage_verified", False)
        if doc_type == "exam" and not coverage_verified:
            return RetrievalResult(
                context_text="لا يوجد حل معتمد ومتحقق منه لهذا السؤال.",
                source=SourceType.CONCEPTUAL,
                score=score,
            )

        source = (
            SourceType.MATCHED_SOLUTION
            if score >= STRONG_MATCH_THRESHOLD
            else SourceType.SIMILAR_TECHNIQUE
        )
        return RetrievalResult(
            context_text=top.text,
            source=source,
            score=score,
            technique_name=top.metadata.get("technique", ""),
        )


def _require_cohere_key() -> str:
    import os

    key = os.environ.get("COHERE_API_KEY")
    if not key:
        raise RetrievalError("COHERE_API_KEY is missing.")
    return key
