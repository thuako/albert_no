import pandas as pd
import time
import datetime

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


def action(bot, update):
    msg = update.message.text
    if msg == 'check':
        rep_msg = 'yes, i am currently running ...'
    elif msg == 'time':
        rep_msg = datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")
    else:
        rep_msg = '???'

    update.message.reply_text(rep_msg)


def compare_df(df, df_old):
    for date_idx in df['date']:
        if date_idx not in list(df_old['date']):
            df_short = df[df['date']==date_idx]
            for idx, row in df_short.iterrows():
                print(row['date'], row['title'], row['timetable'])

updater = Updater('712595804:AAHJZhoIQuMlxwDlW1HpPTY7gstFmc44y20')
dp = updater.dispatcher
dp.add_handler(MessageHandler(Filters.text, action))
updater.start_polling()

areacode = 1
theatercode = 13
screencode = 18

df_old = get_df_theater(areacode, theatercode, screencode)
while True:
    # NOTE: you don't need get_df_theater (get_date_list is enough)
    df = get_df_theater(areacode, theatercode, screencode)
    print('comparing')
    compare_df(df, df_old)
    df_old = df.copy()
    time.sleep(1)
