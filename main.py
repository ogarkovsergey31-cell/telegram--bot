 import os
 import logging
 from telegram import Update
 from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

 logging.basicConfig(level=logging.INFO)

 async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
     await update.message.reply_text('Привет! Я живой! Бот запущен через Render 🚀')

 async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
     await update.message.reply_text(f'Ты написал: {update.message.text}')

 if __name__ == '__main__':
     TOKEN = os.environ.get('BOT_TOKEN')
     app = ApplicationBuilder().token(TOKEN).build()
     
     app.add_handler(CommandHandler("start", start))
     app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
     
     app.run_polling()
