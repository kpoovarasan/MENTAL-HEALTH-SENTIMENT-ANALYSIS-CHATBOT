# 🤖 Telegram Chatbot with BlenderBot & Sentiment Analysis

This project is a Telegram chatbot built using Python that integrates Facebook’s BlenderBot for AI-generated responses and TextBlob for sentiment analysis. It uses NLTK for text preprocessing and supports asynchronous handling via `python-telegram-bot` and `nest_asyncio`. The bot can understand user messages, analyze their emotional tone (positive, negative, neutral), and generate a smart reply. To use it, set your Telegram bot token and model name (e.g., `"facebook/blenderbot-400M-distill"`) in the script. Install required libraries like `transformers`, `textblob`, `nltk`, and run the bot script using Python. This chatbot runs in real time on Telegram and is a simple yet powerful example of combining NLP, deep learning, and chat automation.


---

## ✅ Features

- 💬 Conversational AI using BlenderBot
- 😊 Sentiment analysis using TextBlob
- 🔤 Preprocessing using NLTK
- 📲 Runs on Telegram (real-time interaction)
- 🔁 Supports async handling

---

## ⚙️ Requirements

Install all the required packages:

```bash
pip install python-telegram-bot==20.3
pip install transformers
pip install textblob
pip install nltk
pip install nest_asyncio

##
---

## ✅ Features

- 💬 Conversational AI using BlenderBot
- 😊 Sentiment analysis using TextBlob
- 🔤 Preprocessing using NLTK
- 📲 Runs on Telegram (real-time interaction)
- 🔁 Supports async handling

---

## 💡 Sample Conversation
User: Hello
Bot: Welcome! 😊 How are you feeling today?

User: I'm not feeling good.
Bot: Your sentiment is: negative 😔

---
##🧠 Technologies Used

python-telegram-bot
transformers (for BlenderBot)
textblob (for sentiment analysis)
nltk (for tokenization)
nest_asyncio (for async compatibility)
