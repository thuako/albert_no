# INSTALL python-telegram-bot
from telegram.ext import Updater, CommandHandler
import requests
import re

def get_url():
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    return url


def get_image_url():
    allowed_extension = ['jpg','jpeg','png']
    file_extension = ''
    while file_extension not in allowed_extension:
        url = get_url()
        file_extension = re.search("([^.]*)$",url).group(1).lower()
    return url


def bop(bot, update):
    url = get_image_url()
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)


updater = Updater('712595804:AAHJZhoIQuMlxwDlW1HpPTY7gstFmc44y20')
# Get the dispatcher to register handlers
dp = updater.dispatcher
dp.add_handler(CommandHandler('bop', bop))
# Start the Bot
updater.start_polling()
# Block until you press Ctrl-C or the process receives SIGINT, SIGTERM or
# SIGABRT. This should be used most of the time, since start_polling() is
# non-blocking and will stop the bot gracefully.
updater.idle()
