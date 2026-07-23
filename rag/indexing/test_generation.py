import sys
import os
sys.stdout.reconfigure(encoding='utf-8')
from dotenv import load_dotenv
load_dotenv()

from pathlib import Path
from llama_index.core import StorageContext, load_index_from_storage, Settings
from llama_index.embeddings.google_genai import GoogleGenAIEmbedding
import anthropic

# ========== SETUP ==========

project_root = Path(__file__).resolve().parents[3]
persist_dir = project_root / "Knowledge_Base" / "Math106_index"

Settings.embed_model = GoogleGenAIEmbedding(
    model_name="gemini-embedding-001",
    api_key=os.environ.get("GOOGLE_API_KEY"),
)
storage_context = StorageContext.from_defaults(persist_dir=str(persist_dir))
index = load_index_from_storage(storage_context)
retriever = index.as_retriever(similarity_top_k=1)

client = anthropic.Anthropic()

# ========== SYSTEM PROMPT ==========

SYSTEM_PROMPT = """You are a tutor for MATH106 (Integral Calculus) students at King Saud University.

CRITICAL RULES:
- You will be given a verified solution from the course's solution bank. Use it as your ONLY source of truth for the method and final answer.
- Never invent a different method or answer than what's in the provided solution.
- Always state the rule/technique being used FIRST, before any steps.
- Show every step explicitly — never skip from problem to answer.
- Match the KSU grading culture: a correct method with a small arithmetic slip earns most marks; a correct answer with no stated rule earns almost nothing.
- Keep your tone like a knowledgeable senior student, not a generic AI assistant.
- Respond in clear, well-formatted text suitable for Telegram (no LaTeX rendering, no markdown headers with #)."""

# ========== QUERY ==========

student_question = "Evaluate the integral of x e^{-x} dx"

nodes = retriever.retrieve(student_question)
top_match = nodes[0]

print("Matched file:", top_match.metadata.get("file_name", "unknown"))
print("Score:", top_match.score)
print("\n--- Sending to Claude ---\n")

user_message = f"""Student's question: {student_question}

Here is the verified solution from the course's solution bank:

{top_match.text}

Explain this to the student following the rules above."""

response = client.messages.create(
    model="claude-sonnet-4-6", # <-- قم بتعديل هذا السطر فقط
    max_tokens=1000,
    system=SYSTEM_PROMPT,
    messages=[
        {"role": "user", "content": user_message}
    ]
)

print(response.content[0].text)