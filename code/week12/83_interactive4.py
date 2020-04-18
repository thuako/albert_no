# INSTALL python-telegram-bot
from telegram.ext import Updater, InlineQueryHandler, Filters, MessageHandler


def action(bot, update):
    msg = update.message.text
    print(msg)
    update.message.reply_text(msg + ' is amazing')


updater = Updater('712595804:AAHJZhoIQuMlxwDlW1HpPTY7gstFmc44y20')
dp = updater.dispatcher
dp.add_handler(MessageHandler(Filters.text, action))
updater.start_polling()
updater.idle()
