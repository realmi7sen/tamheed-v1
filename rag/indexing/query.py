import sys
import os
sys.stdout.reconfigure(encoding='utf-8')
from dotenv import load_dotenv
load_dotenv()

from pathlib import Path
from llama_index.core import StorageContext, load_index_from_storage, Settings
from llama_index.embeddings.google_genai import GoogleGenAIEmbedding

project_root = Path(__file__).resolve().parents[3]
persist_dir = project_root / "Knowledge_Base" / "Math106_index"

Settings.embed_model = GoogleGenAIEmbedding(
    model_name="gemini-embedding-001",
    api_key=os.environ.get("GOOGLE_API_KEY"),
)
storage_context = StorageContext.from_defaults(persist_dir=str(persist_dir))
index = load_index_from_storage(storage_context)

print("Total chunks in index:", len(index.docstore.docs))

retriever = index.as_retriever(similarity_top_k=5)
nodes = retriever.retrieve("احسب تكامل x e^{-x}")

for node in nodes:
    print("---")
    print("File:", node.metadata.get("file_name", "unknown file"))
    print("Score:", node.score)
    print("Content preview:", node.text[:300])