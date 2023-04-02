import logging
import os , subprocess
from telegram import Update
from telegram.ext import  filters , MessageHandler , ApplicationBuilder, ContextTypes, CommandHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def down(update : Update , context: ContextTypes.DEFAULT_TYPE):
    backup_dir="/music2/"+ str(update.effective_chat.id) + "backupmusic"
    if not (os.path.isfile(backup_dir)) :
        open(backup_dir , 'w')
    for filename in os.listdir('/music'):
        data_base = open(backup_dir , 'r+') 
        if  filename  not in  data_base.read():
            await context.bot.send_document(chat_id=update.effective_chat.id , document=open(os.path.join(os.getcwd(), "/music/"+filename), 'rb'))
            print(filename , file = data_base)
            data_base.close()


async def get(update: Update , context : ContextTypes.DEFAULT_TYPE):
    os.chdir('/music')
    subprocess.call(['scdl', '-l', 'https://soundcloud.com/arpjoker-82' , '-f' , '-c' ])
    await down(update , context)
    await context.bot.send_message(chat_id=update.effective_chat.id, text="done")



async def single(update: Update , context : ContextTypes.DEFAULT_TYPE):
    link = " ".join(context.args)
    os.chdir('/tmp/single')
    try:
        subprocess.call(['scdl', '-l', link ])
        await context.bot.send_message(chat_id=update.effective_chat.id, text="track downloaded")
        for filename in os.listdir('/tmp/single'):
            await context.bot.send_document(chat_id=update.effective_chat.id , document=open(os.path.join(os.getcwd(), filename), 'rb'))
            subprocess.call(['rm' , '-f' , filename])
    except:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="error while sending track")



async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=" type /down to get all of my liked songs , be aware :)  \n /get for newer songs \n /single <link> for single song")
    print(update.effective_chat.id)

if __name__ == '__main__':
    application = ApplicationBuilder().token('5822488993:AAEez4o_o0rRQ4ODq7OF4fHA1dE').build()
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND) , echo)
    start_handler = CommandHandler('start', start)
    down_handler = CommandHandler('down' , down)
    get_handler = CommandHandler('get' , get)
    single_handler = CommandHandler('single' , single)
    application.add_handler(down_handler)
    application.add_handler(start_handler) 
    application.add_handler(echo_handler)
    application.add_handler(get_handler)
    application.add_handler(single_handler)
    application.run_polling()

# add two numb