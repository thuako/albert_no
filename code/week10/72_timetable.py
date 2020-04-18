import pandas as pd
import time

from cgv_util import get_date_list


# for 72_timetable.py
def get_title_and_time(areacode, theatercode, date):
    date_url = get_url(areacode, theatercode, date)
    date_soup = get_soup(date_url)

    showtimes = date_soup.find('div', class_='sect-showtimes')
    coltimes = showtimes.find_all('div', class_='col-times')

    raw_df = []
    for coltime in coltimes:
        title = coltime.find('a', href=True)
        title_str = title.get_text().strip()
        typehalls = coltime.find_all('div', class_='type-hall')
        for typehall in typehalls:
            # get halltype
            infohall = typehall.find('div', class_='info-hall')
            infohall_li = infohall.find_all('li')
            halltype = infohall_li[1].get_text().strip()

            # get timetable
            timeslots = typehall.find_all('em')
            timetable = [timeslot.get_text() for timeslot in timeslots]
            raw_df.append([date, title_str, halltype, timetable])
    return pd.DataFrame(raw_df, columns=["date", "title", "hall_type", "timetable"])


areacode = 1
theatercode = 13
date_list = get_date_list(areacode, theatercode)

desired_width = 640
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns',15)

df_list = []
for date in date_list:
    time.sleep(0.5)
    df_date = get_title_and_time(areacode, theatercode, date)
    df_list.append(df_date)

df = pd.concat(df_list, ignore_index=True)
print(df)


