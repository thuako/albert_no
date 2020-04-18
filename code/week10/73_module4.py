import pandas as pd
import time

from cgv_util import get_date_list, get_title_and_time


desired_width = 640
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns',15)

areacode = 1
theatercode = 13
date_list = get_date_list(areacode, theatercode)

df_list = []
for date in date_list:
    time.sleep(0.5)
    df_date = get_title_and_time(areacode, theatercode, date)
    df_list.append(df_date)

df = pd.concat(df_list, ignore_index=True)
print(df)


