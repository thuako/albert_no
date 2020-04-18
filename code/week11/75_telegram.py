# Find BotFather
# /newbot
# name: hongik-sample
# username: hongikee_bot
# token: 712595804:AAHJZhoIQuMlxwDlW1HpPTY7gstFmc44y20
# Find your bot and start
# https://api.telegram.org/bot<yourtoken>/getUpdates
# get your chatid 898518917

import requests


def telegram_bot_sendtext(bot_message):
    bot_token = '712595804:AAHJZhoIQuMlxwDlW1HpPTY7gstFmc44y20'
    bot_chatID = '898518917'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()


response = telegram_bot_sendtext('you are a good man')
