import logging
import os , subprocess ,time
from telegram import Update , KeyboardButton ,ReplyKeyboardMarkup 
from telegram.ext import  filters , MessageHandler , ApplicationBuilder, ContextTypes, CommandHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update , context: ContextTypes.DEFAULT_TYPE):
    if (update.effective_chat.id == 445634207):
        buttons = [[KeyboardButton("SO_Status")],[KeyboardButton("SO_Login")]]
        await context.bot.send_message(chat_id = 445634207 , text = "Welcome...Me!" , reply_markup = ReplyKeyboardMarkup(buttons))
    else:
        await context.bot.send_message(chat_id = update.effective_chat.id , text = "you are not allowed to use this bot yet!")

#def log (update : update , context : Callbac    )

if __name__ == '__main__':
    BOT_TOKEN = os.environ['BOT_TOKEN']
    application = ApplicationBuilder().token(BOT_TOKEN).build()
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler) 
    #application.add_handler(MessageHandler(filters.text, log))     

    application.run_polling()
    os.putenv(name, value)