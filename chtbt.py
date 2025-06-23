# Required imports
import asyncio
import re
import nltk
from nltk.tokenize import word_tokenize
from textblob import TextBlob
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
import nest_asyncio
from transformers import BlenderbotTokenizer, BlenderbotForConditionalGeneration

# Apply nest_asyncio for Jupyter Notebook or nested loops
nest_asyncio.apply()

# Download necessary NLTK data (run once)
nltk.download("punkt")

# 🔐 Telegram Bot Token
TOKEN = "8161353864:AAEZ3aOnY3YnpvO6luRdpjDMDc5tpy3k6n4"

# ✅ Load BlenderBot locally
model_name = "facebook/blenderbot-400M-distill"
tokenizer = BlenderbotTokenizer.from_pretrained(model_name)
model = BlenderbotForConditionalGeneration.from_pretrained(model_name)

# 1️⃣ Preprocessing Function
def preprocess_text(text):
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
    text = text.lower().strip()
    words = word_tokenize(text)
    return " ".join(words)

# 2️⃣ Sentiment Analysis
def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment_score = blob.sentiment.polarity
    if sentiment_score > 0:
        return "positive 😊"
    elif sentiment_score < 0:
        return "negative 😔"
    else:
        return "neutral 😐"

# 3️⃣ AI Response using Local BlenderBot
def generate_ai_response(user_text):
    inputs = tokenizer([user_text], return_tensors="pt")
    reply_ids = model.generate(**inputs)
    reply = tokenizer.batch_decode(reply_ids, skip_special_tokens=True)[0]
    return reply

# 4️⃣ Telegram Bot Handlers
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Hello! How are you feeling today? 😊")

async def handle_message(update: Update, context: CallbackContext):
    user_text = update.message.text.lower().strip()

    if user_text in ["hi", "hello", "hey"]:
        await update.message.reply_text("Welcome! 😊 How are you feeling today?")
        return

    clean_text = preprocess_text(user_text)
    sentiment = analyze_sentiment(clean_text)
    ai_response = generate_ai_response(clean_text)

    response = f"Your sentiment is: {sentiment}\n\n{ai_response}"
    await update.message.reply_text(response)

# 5️⃣ Main Bot Function
async def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("🤖 Telegram bot is running...")
    await app.run_polling()

# 6️⃣ Run the Bot
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    if loop.is_running():
        loop.create_task(main())
    else:
        loop.run_until_complete(main())
