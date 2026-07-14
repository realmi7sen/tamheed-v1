from pathlib import Path
from llama_index.core import SimpleDirectoryReader

project_root = Path(__file__).resolve().parents[3]
data_dir = project_root / "Knowledge_Base" / "Math106"

print("Knowledge Base:", data_dir)
print("Exists:", data_dir.exists())

reader = SimpleDirectoryReader(
    input_dir=str(data_dir),
    recursive=True,   # <-- أضف هذا السطر
)

documents = reader.load_data()

print(f"Loaded {len(documents)} documents")