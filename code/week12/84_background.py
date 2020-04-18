import time
from telegram.ext import Updater, Filters, MessageHandler, CommandHandler


def action(bot, update):
    msg = update.message.text
    print(msg)
    update.message.reply_text(msg + ' is amazing')


updater = Updater('712595804:AAHJZhoIQuMlxwDlW1HpPTY7gstFmc44y20')
chat_id = '898518917'

dp = updater.dispatcher
dp.add_handler(MessageHandler(Filters.text, action))
updater.start_polling()

while True:
    updater.bot.send_message(chat_id, 'hi')
    time.sleep(1)
