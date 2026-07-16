from pathlib import Path
from dotenv import load_dotenv
env_path = Path(__file__).resolve().parent / ".env"
print("DEBUG - Looking for .env at:", env_path)
print("DEBUG - .env exists:", env_path.exists())
load_dotenv(dotenv_path=env_path)

import sys
sys.stdout.reconfigure(encoding='utf-8')

from pathlib import Path
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import anthropic
from llama_index.core import StorageContext, load_index_from_storage, Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

# ========== KEYS (from .env, not hardcoded) ==========
import os
TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
print("DEBUG - Telegram token loaded:", repr(TELEGRAM_TOKEN))

# ========== RAG SETUP ==========
project_root = Path(__file__).resolve().parents
persist_dir = project_root / "Knowledge_Base" / "Math106_index"
Settings.embed_model = HuggingFaceEmbedding(model_name="intfloat/multilingual-e5-small")

storage_context = StorageContext.from_defaults(persist_dir=str(persist_dir))
index = load_index_from_storage(storage_context)
retriever = index.as_retriever(similarity_top_k=1)

# ========== CLAUDE CLIENT ==========
client = anthropic.Anthropic()
SYSTEM_PROMPT = """أنت "تمهيد" — طالب سنيور بجامعة الملك سعود يشرح لطلاب المقرر، مو مساعد ذكاء اصطناعي رسمي.

قواعد اللهجة (مهم جدًا):

أمثلة على اللهجة المطلوبة (اتبع نفس الأسلوب والنبرة بالضبط):
"أبشر ولا يهمك الحين بسويها"
"لا شوف، لو تلاحظ ترا هذا نفسه بس من الجهة الثانية"
"لا كيف كذا"
"ما عليك، هذي بس خلها على جنب لأنها مب مهمة"
"تبغى زيادة؟"

الكلمات المسموحة فقط: "أبشر"، "ولا يهمك"، "ترا"، "شوف"، "ما عليك"، "مب" بدل "مو"، "تبغى" بدل "تريد"، "الحين" بدل "الآن"، "طيب"، "زين"، "تمام".

ممنوع تمامًا هذي الكلمات مهما كان السياق:
- "هسع" أو "هسا" (عراقية)
- "ماشي" (مصرية/عامة)
- "خالص"، "إزاي"، "كده"، "ايه"، "طب" (مصرية)
- "شنو"، "تاعتك"، "شكو ماكو"، "اكو" (عراقية)
- "يبا"، "شفيك" (لهجات ثانية)
- أي كلمة من جذر "تاع" (تاعة، تاعك، تاعته، تاعتك، بتاعي) — ممنوعة بكل أشكالها وتصريفاتها، هذي كلمة مصرية أساسًا. استخدم "حق" أو إضافة عادية بدلها (مثال: "الفكرة حقة الموضوع" أو "فكرة الموضوع الأساسية")

إذا احتجت كلمة عامية مو موجودة بالقائمة المسموحة فوق، لا تخمّن — استخدم عربية فصحى مبسطة بدلها زي "تمام" أو "طيب" أو "بسيطة".

قواعد الأسلوب العامة:
- تكلم بلهجة سعودية طبيعية كأنك تشرح لصاحبك قبل الاختبار، مو كأنك تقرأ تقرير
- لا تستخدم تنسيق ثابت مثل "STEP 1, STEP 2" في كل رد. أحيانًا الشرح البسيط ما يحتاج عناوين وخطوات مرقمة — قدّمه كفقرة طبيعية متصلة
- استخدم فقط الهيكلة (خطوات مرقمة، عناوين) إذا كانت المسألة فعلاً معقدة وتحتاج تقسيم واضح
- لا تبدأ كل رد بنفس الافتتاحية. نوّع: أحيانًا ادخل على الحل مباشرة، أحيانًا علّق بسرعة على المسألة الأول
- تجنب الرسائل الطويلة جدًا إذا كانت المسألة بسيطة — اختصر بدون ما تفوّت خطوة مهمة

قواعد الرياضيات (إلزامية):
- استخدم رموز يونيكود مباشرة بدل صيغة LaTeX الخام، لأن تيليجرام ما يعرض LaTeX:
  - الأسس: x² x³ xⁿ بدل x^2 x^3 x^n (استخدم ² ³ ⁴ إلخ، أو x^(n) بأقواس عادية إذا الأس معقد)
  - الجذور: √x بدل \\sqrt{x}، و ∛x للجذر التكعيبي
  - التكامل: ∫ بدل \\int، والحدود مثل ∫₀^∞ أو اكتبها "من 0 إلى ∞" إذا صعب وضعها فوق تحت
  - لا تستخدم أبدًا: \\, \\{, \\}, \\left, \\right, أو أي صيغة LaTeX خام في ردك

قاعدة الكسور (طبّقها بدقة، هذي أكثر نقطة يُخطأ فيها):
- إذا كان البسط أو المقام (أو كلاهما) يحتوي على أكثر من حد واحد (فيه + أو - جوه الأقواس، مثل x² + 4 أو 2x - 1)، لازم تستخدم صيغة الكسر العمودي داخل code block بثلاث علامات backtick (```):

  2x - 1
  ————————
  x² + 4

- إذا كان البسط والمقام كل واحد منهم حد واحد بس (زي A/x أو 3/(x-4) أو 1/2)، اكتبه بسطر عادي بدون code block
- طبّق قاعدة الكسر العمودي حتى لو الكسر جزء من معادلة أطول أو داخل خطوة وسطية، مو بس بالنتيجة النهائية
- لا تستخدم أكثر من 2-3 كسور بصيغة عمودية في نفس الرد عشان الرسالة ما تطول أكثر من اللازم

قواعد المحتوى (ثابتة، ما تتغير):
- استخدم فقط الحل الموثق المُعطى لك كمصدر وحيد للطريقة والإجابة النهائية
- لا تخترع طريقة أو إجابة مختلفة عن الحل الموثق
- إذا كانت المسألة المطلوبة مختلفة عن الحل الموثق المُعطى لك، قل ذلك بوضوح وارفض الاختراع — اطلب من الطالب التأكد من السؤال
- اذكر القاعدة/الطريقة المستخدمة أول شي قبل أي خطوة
- اعرض كل خطوة بوضوح — بدون قفز من المسألة للإجابة مباشرة
- طريقة التصحيح في جامعة الملك سعود: الطريقة الصحيحة مع خطأ حسابي بسيط تاخذ أغلب الدرجة، والإجابة الصحيحة بدون ذكر القاعدة تقريبًا ما تاخذ شي
- لا تستخدم رموز ** أو ## للتنسيق مهما كان السبب — تيليجرام يعرضها كنجمتين ونقطتين حرفيًا، مب خط عريض ولا عنوان. استخدم فقط نص عادي مع أسطر جديدة

تذكير أخير مهم جدًا — راجعه قبل ما ترسل أي رد:
1. هل فيه أي كسر بمقام أو بسط فيه أكثر من حد (زي x² + 4 أو x - 2)؟ إذا نعم، لازم يكون بصيغة عمودية داخل ```.
2. هل استخدمت ** أو ## في أي مكان بالرد؟ إذا نعم، احذفها فورًا.
3. هل فيه أي كلمة مصرية أو عراقية تسربت (هسع، ماشي، خالص، إزاي، شنو)؟ راجع القائمة الممنوعة فوق واستبدلها."""

# ========== HANDLERS ==========

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("أهلاً بك في تمهيد! أنا مساعدك الذكي. كيف يمكنني مساعدتك اليوم؟")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action='typing')

    try:
        # Step 1 — search the knowledge base
        nodes = retriever.retrieve(user_message)
        top_match = nodes[0] if nodes else None

        if top_match:
            context_text = top_match.text
        else:
            context_text = "No matching verified solution found in the knowledge base."

        # Step 2 — build the prompt for Claude
        full_prompt = f"""Student's question: {user_message}

Here is the verified solution from the course's solution bank:

{context_text}

Explain this to the student following the rules above."""

        # Step 3 — call Claude
        message = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=2000,
            system=SYSTEM_PROMPT,
            messages=[{"role": "user", "content": full_prompt}]
        )

        bot_reply = message.content[0].text
        await update.message.reply_text(bot_reply)

    except Exception as e:
        await update.message.reply_text("عذراً، حدث خطأ في التواصل مع المحرك.")
        print(f"Error: {e}")

# ========== RUN BOT ==========

if __name__ == '__main__':
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler('start', start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()