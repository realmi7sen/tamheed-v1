from pathlib import Path

from llama_index.core import Settings, StorageContext, load_index_from_storage
from llama_index.embeddings.google_genai import GoogleGenAIEmbedding

from utils.errors import RetrievalError
from utils.types import RetrievalResult, SourceType


# عتبات القرار — معزولة كي يسهل ضبطها لاحقًا.
MATCH_THRESHOLD = 0.55
STRONG_MATCH_THRESHOLD = 0.80


class KnowledgeService:
    """يغلّف بناء الفهرس والاسترجاع وقرار نوع الدليل."""

    def __init__(self, persist_dir: Path, top_k: int = 3):
        Settings.embed_model = GoogleGenAIEmbedding(
            model_name="gemini-embedding-001",
            api_key=_require_google_key(),
        )
        storage_context = StorageContext.from_defaults(persist_dir=str(persist_dir))
        index = load_index_from_storage(storage_context)
        self._retriever = index.as_retriever(similarity_top_k=top_k)

    async def search(self, query: str) -> RetrievalResult:
        try:
            nodes = await self._retriever.aretrieve(query)
        except Exception as error:
            raise RetrievalError(str(error)) from error

        # استبعد نتائج الاختبارات غير المتحقق منها قبل أي قرار
        valid = [
            n for n in nodes
            if not (
                n.metadata.get("doc_type", "") == "exam"
                and not n.metadata.get("coverage_verified", False)
            )
        ]

        top = valid[0] if valid else None
        score = float(getattr(top, "score", 0) or 0) if top else 0.0

        print(f"[RETRIEVAL] nodes={len(nodes)} valid={len(valid)} score={score:.3f}")
        

        if not top or score < MATCH_THRESHOLD:
            return RetrievalResult(
                context_text="لا يوجد ملف معتمد مطابق لهذا السؤال في بنك الحلول.",
                source=SourceType.CONCEPTUAL,
                score=score,
            )

        # ضم النتائج القريبة من الأفضل (فرق ≤ 0.05) كسياق إضافي — بحد أقصى نتيجتين إضافيتين
        context_parts = [top.text]
        for n in valid[1:3]:
            n_score = float(getattr(n, "score", 0) or 0)
            if n_score >= MATCH_THRESHOLD and (score - n_score) <= 0.05:
                context_parts.append(n.text)

        source = (
            SourceType.MATCHED_SOLUTION
            if score >= STRONG_MATCH_THRESHOLD
            else SourceType.SIMILAR_TECHNIQUE
        )
        return RetrievalResult(
            context_text="\n\n---\n\n".join(context_parts),
            source=source,
            score=score,
            technique_name=top.metadata.get("technique", ""),
        )


def _require_google_key() -> str:
    import os

    key = os.environ.get("GOOGLE_API_KEY")
    if not key:
        raise RetrievalError("GOOGLE_API_KEY is missing.")
    return key