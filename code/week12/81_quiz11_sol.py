# 1. get all IMAX movies with timetable of CGV Yongsan or Wangsimni based on telegram message

# 2 1. get all (or all IMAX) movies with timetable of CGV Yongsan or Wangsimni based on telegram message
import pandas as pd
import time

from cgv_util_new import get_date_list, get_title_and_time
from telegram.ext import Updater, Filters, MessageHandler


def get_df_theater(areacode, theatercode, screencode):
    date_list = get_date_list(areacode, theatercode)

    df_list = []
    for date in date_list:
        time.sleep(0.5)
        df_date = get_title_and_time(areacode, theatercode, date, screencodes=screencode)  # TBD ADD screencode
        df_list.append(df_date)

    df_theater = pd.concat(df_list, ignore_index=True)
    return df_theater


def get_df_all(codes):
    df_list = []
    for code in codes:
        df_theater = get_df_theater(code['areacode'], code['theatercode'], code['screencode'])
        df_list.append(df_theater)
    df_all = pd.concat(df_list, ignore_index=True)
    return df_all


def action(bot, update):
    areacode = 1
    msg = update.message.text
    msg_list = msg.split()
    screencode_dict = {13: 18, 74: 9}
    try:
        theatercode = int(msg_list[0])
        if len(msg_list) == 2 and msg_list[1] == 'IMAX':
            screencode = screencode_dict[theatercode]
        elif len(msg_list) == 1 and theatercode in [13, 74]:
            screencode = None
        else:
            raise ValueError

        print(f'Running get_df_theater for theatercode={theatercode}, screencode={screencode}')
        df_theater = get_df_theater(areacode, theatercode, screencode)
        print('Done get_df_theater')
        # You may want to remove index
        # You may want to send multiple messages (in organized fashion)
        msg = df_theater.to_string()
        update.message.reply_text(msg)
    except ValueError:
        msg = 'Wrong Input'
        update.message.reply_text(msg)
    print(msg)


# codes = [{'areacode': 1, 'theatercode': 13, 'screencode': 18},
#          {'areacode': 1, 'theatercode': 74, 'screencode': 9},
#          ]


updater = Updater('712595804:AAHJZhoIQuMlxwDlW1HpPTY7gstFmc44y20')
dp = updater.dispatcher
dp.add_handler(MessageHandler(Filters.text, action))
updater.start_polling()
updater.idle()
