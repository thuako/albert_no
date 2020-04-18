import telepot
from telepot.loop import MessageLoop


def action(msg):
    msg_txt = msg['text']  # get text of message
    print(msg_txt)

my_bot = telepot.Bot('712595804:AAHJZhoIQuMlxwDlW1HpPTY7gstFmc44y20')  # give bot a token

MessageLoop(my_bot, action).run_as_thread()  # checking message in the background
print('Up and Running....')

while True:
    pass  # keep running the code