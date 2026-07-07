from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import os

TOKEN = os.getenv("8910210299:AAG0gmaewKaQ-sm4UU__uSaccWH3eIg-25I")

WELCOME_TEXT = """
👋 Приветствую вас!

Если у вас спамблок и вы не можете написать первыми, то напишите в этого бота вам @username, и я отвечу вам как можно скорее.

С уважением,
MoonLight 🌙
"""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(WELCOME_TEXT)

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("Бот запущен ✅")
    app.run_polling()

if __name__ == "__main__":
    main()
