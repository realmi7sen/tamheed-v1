from dotenv import load_dotenv
load_dotenv()

import os
import re
from pathlib import Path

from llama_index.core import SimpleDirectoryReader, VectorStoreIndex, Settings
from llama_index.core.node_parser import SentenceSplitter
from llama_index.embeddings.cohere import CohereEmbedding

# ========= CONFIG =========

project_root = Path(__file__).resolve().parents[2]
data_dir = project_root / "Knowledge_Base" / "math106"
persist_dir = project_root / "Knowledge_Base" / "Math106_index"

print(f"Knowledge Base: {data_dir}")

# ========= EMBEDDING MODEL =========

Settings.embed_model = CohereEmbedding(
    api_key=os.environ["COHERE_API_KEY"],
    model_name="embed-multilingual-v3.0",
    input_type="search_document",
)

Settings.node_parser = SentenceSplitter(chunk_size=8192, chunk_overlap=0)

# ========= METADATA =========

SECTION_TECHNIQUES = {
    "7_1": "التكامل بالتجزئة",
    "7_2": "تكاملات الدوال المثلثية",
    "7_3": "التعويض المثلثي",
    "7_4": "الكسور الجزئية",
    "7_5": "تكاملات متنوعة",
    "7_7": "التكاملات المعتلة",
}


def file_metadata(file_path: str) -> dict:
    path = Path(file_path)
    parts_lower = [p.lower() for p in path.parts]
    joined = " ".join(parts_lower)
    meta: dict = {"file_name": path.name}

    if "exams" in parts_lower:
        meta["doc_type"] = "exam"
        meta["coverage_verified"] = "current" in parts_lower
    elif "soloutions" in joined or path.name.startswith("ex_"):
        meta["doc_type"] = "solution"
        meta["coverage_verified"] = True
    else:
        meta["doc_type"] = "section"
        meta["coverage_verified"] = True

    match = re.search(r"7[_.]\d", path.name.replace(".", "_"))
    if not match:
        for part in parts_lower:
            m = re.search(r"7[_.]\d", part.replace(".", "_"))
            if m:
                match = m
                break
    if match:
        section = match.group(0).replace(".", "_")
        meta["section"] = section
        meta["technique"] = SECTION_TECHNIQUES.get(section, "")

    return meta


# ========= LOAD DOCUMENTS =========

reader = SimpleDirectoryReader(
    input_dir=str(data_dir),
    recursive=True,
    required_exts=[".md"],
    file_metadata=file_metadata,
)
documents = reader.load_data()
print(f"Loaded {len(documents)} documents")

# ========= BUILD INDEX =========

print("Building index...")
index = VectorStoreIndex.from_documents(documents)
print("Saving index...")
index.storage_context.persist(persist_dir=str(persist_dir))
print("Done!")
print(f"Saved to: {persist_dir}")