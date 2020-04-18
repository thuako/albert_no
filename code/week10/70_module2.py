import pandas as pd
import requests
import time

from bs4 import BeautifulSoup


def get_soup(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup


def get_url(areacode, theatercode, date=None, screencodes=None):
    url = f"http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode={areacode:02d}&theatercode={theatercode:04d}"
    if date:
        url += f"&date={date}"
    if screencodes:
        url += f"&screencodes={screencodes:03d}"
    return url


def get_date_list(areacode, theatercode):
    url_yongsan = get_url(areacode, theatercode)
    soup = get_soup(url_yongsan)

    schedule = soup.find('div', class_='item-wrap')
    a_list = schedule.find_all('a', href=True)

    date_list = []
    for a_item in a_list:
        href_str = a_item['href']
        date_idx = href_str.find('date=')
        date_str = href_str[date_idx+5:date_idx+13]
        date_list.append(date_str)
    return date_list


def get_title_list(areacode, theatercode, date):
    date_url = get_url(areacode, theatercode, date)
    date_soup = get_soup(date_url)

    showtimes = date_soup.find('div', class_='sect-showtimes')
    coltimes = showtimes.find_all('div', class_='col-times')

    title_list = []
    for coltime in coltimes:
        title = coltime.find('a', href=True)
        title_str = title.get_text().strip()
        title_list.append(title_str)
    return title_list


areacode = 1
theatercode = 13
date_list = get_date_list(areacode, theatercode)

raw_df = []
for date in date_list:
    time.sleep(0.5)
    title_list = get_title_list(areacode, theatercode, date)
    print(date, title_list)

print(raw_df)