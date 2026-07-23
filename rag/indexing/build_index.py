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
from llama_index.embeddings.google_genai import GoogleGenAIEmbedding

Settings.embed_model = GoogleGenAIEmbedding(
    model_name="gemini-embedding-001",
    api_key=os.environ["GOOGLE_API_KEY"],
    embed_batch_size=64,
)

Settings.node_parser = SentenceSplitter(chunk_size=1024, chunk_overlap=200)

# ========= METADATA =========

SECTION_TECHNIQUES = {
    # Chapter 4
    "4_1": "Antiderivatives and indefinite integrals",
    "4_2": "Change of variables in indefinite integrals",
    "4_3": "Summation notation and area",
    "4_4": "The definite integral",
    "4_5": "Properties of definite integral",
    "4_6": "The fundamental theorem of calculus",
    "4_7": "Numerical integration",
    # Chapter 6
    "6_2": "The natural logarithm function",
    "6_3": "The exponential function",
    "6_4": "Integration using natural logarithm and exponential function",
    "6_5": "General exponential function and logarithm function",
    "6_7": "Inverse trigonometric functions",
    "6_8": "Hyperbolic and inverse hyperbolic functions",
    "6_9": "Indeterminate forms and L'Hopital's rule",
    # Chapter 7
    "7_1": "التكامل بالتجزئة",
    "7_2": "تكاملات الدوال المثلثية",
    "7_3": "التعويض المثلثي",
    "7_4": "الكسور الجزئية",
    "7_5": "تكاملات متنوعة",
    "7_7": "التكاملات المعتلة",
    # Chapter 5
    "5_1": "Area between curves",
    "5_2": "Volume by disk or washer method",
    "5_3": "Volume by cylindrical shells method",
    "5_5": "Arc length and surface of revolution",
    # Chapter 9
    "9_1": "Parametric equations",
    "9_2": "Arc length and surface area",
    "9_3": "Polar coordinates",
    "9_4": "Integrals in polar coordinates",
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

    # تم تحديث الـ regex ليغطي الفصول المطلوبة للفاينل: 4, 5, 6, 7, 9
    match = re.search(r"[45679][_.]\d", path.name.replace(".", "_"))
    if not match:
        for part in parts_lower:
            m = re.search(r"[45679][_.]\d", part.replace(".", "_"))
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
import time

BATCH = 30
index = VectorStoreIndex.from_documents(documents[:BATCH])
print(f"indexed {BATCH}/{len(documents)}")

from llama_index.core.node_parser import SentenceSplitter
splitter = SentenceSplitter(chunk_size=1024, chunk_overlap=200)

for i in range(BATCH, len(documents), BATCH):
    time.sleep(30)
    nodes = splitter.get_nodes_from_documents(documents[i:i + BATCH])
    index.insert_nodes(nodes)
    print(f"indexed {min(i + BATCH, len(documents))}/{len(documents)}")
index.storage_context.persist(persist_dir=str(persist_dir))
print("Done!")
print(f"Saved to: {persist_dir}")