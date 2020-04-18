import telepot
from telepot.loop import MessageLoop


my_bot = telepot.Bot('712595804:AAHJZhoIQuMlxwDlW1HpPTY7gstFmc44y20')  # give bot a token


def action(msg):
    chat_id = 898518917
    msg_txt = msg['text']  # get text of message
    my_bot.sendMessage(chat_id, msg_txt+' is amazing')
    print(msg_txt)


MessageLoop(my_bot, action).run_as_thread()  # checking message in the background
print('Up and Running....')

while True:
    pass  # keep running the code