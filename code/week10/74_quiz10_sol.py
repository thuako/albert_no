# 1. get all IMAX movies with timetable of CGV Yongsan and Wangsimni
# 2. get all IMAX movies with timetable of CGV Yongsan and Wangsimni every minute (use try/except)
import pandas as pd
import time

from cgv_util_new import get_date_list, get_title_and_time


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
    return(df_all)


desired_width = 640
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', 15)

codes = [{'areacode': 1, 'theatercode': 13, 'screencode': 18},
         {'areacode': 1, 'theatercode': 74, 'screencode': 9},
         ]

while True:
    time.sleep(5)
    df = get_df_all(codes)
    print(df)



