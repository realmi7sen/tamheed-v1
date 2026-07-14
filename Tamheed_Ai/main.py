import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import anthropic
import os
from anthropic import Anthropic

# 1. مفاتيحك السرية
TELEGRAM_TOKEN = '8788176562:AAHxxwA7yDjxm2GvPZylIb6iAHnamnZWfDo'
ANTHROPIC_API_KEY = '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'

# 2. تشغيل محرك Claude
client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("أهلاً بك في  تمهيد! أنا مساعدك الذكي . كيف يمكنني مساعدتك اليوم؟")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action='typing')
    
    try:
        # إرسال السؤال لـ Claude
        message = client.messages.create(
            model="claude-sonnet-4-6", # موديل قوي ومتوازن
            max_tokens=1000,
            system="أنت 'محرك تمهيد'، مساعد أكاديمي ذكي. أجب بوضوح وشرح بسيط.",
            messages=[{"role": "user", "content": user_message}]
        )
        
        bot_reply = message.content[0].text
        await update.message.reply_text(bot_reply)
        
    except Exception as e:
        await update.message.reply_text("عذراً، حدث خطأ في التواصل مع المحرك.")
        print(f"Error: {e}")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler('start', start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()
    
    
    
    
    
    
    
    #Services File
    
    from services import pdf_to_pure_text

lecture_text = pdf_to_pure_text("path_to_your_file.pdf")
print(lecture_text[:500]) 

#Anthropic API 


client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)

message = client.messages.create(
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": "Hello, Claude",
        }
    ],

    model="claude-opus-4-6",
)

print(message.content)