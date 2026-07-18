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
# Must match retrieval/knowledge.py: embed-multilingual-v3.0 (1024-dim).
# input_type differs on purpose: "search_document" for indexing,
# "search_query" at query time.

Settings.embed_model = CohereEmbedding(
    api_key=os.environ["COHERE_API_KEY"],
    model_name="embed-multilingual-v3.0",
    input_type="search_document",
)

Settings.node_parser = SentenceSplitter(chunk_size=8192, chunk_overlap=0)

# ========= LOAD DOCUMENTS =========

reader = SimpleDirectoryReader(
    input_dir=str(data_dir),
    recursive=True,
    required_exts=[".md"],
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