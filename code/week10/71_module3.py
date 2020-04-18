import time

from cgv_util import get_date_list, get_title_list


areacode = 1
theatercode = 13
date_list = get_date_list(areacode, theatercode)

for date in date_list:
    time.sleep(0.5)
    title_list = get_title_list(areacode, theatercode, date)
    print(date, title_list)

