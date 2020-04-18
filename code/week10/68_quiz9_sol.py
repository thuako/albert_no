import pandas as pd
import requests
import time

from bs4 import BeautifulSoup

# 1. Print all movie titles with dates of Yongsan CGV
url = "http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0013"

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

schedule = soup.find('div', class_='item-wrap')
a_list = schedule.find_all('a', href=True)

date_list = []
for a_item in a_list:
    href_str = a_item['href']
    date_idx = href_str.find('date=')
    date_str = href_str[date_idx+5:date_idx+13]
    date_list.append(date_str)

raw_df = []
for date in date_list:
    time.sleep(0.5)
    date_url = url + "&date=" + date
    print(date_url)
    date_page = requests.get(date_url)
    date_soup = BeautifulSoup(date_page.content, 'html.parser')

    showtimes = date_soup.find('div', class_='sect-showtimes')
    coltimes = showtimes.find_all('div', class_='col-times')

    for coltime in coltimes:
        title = coltime.find('a', href=True)
        title_str = title.get_text().strip()
        print(date, title_str)
        raw_df.append([date, title_str])

# 2. Create a dataframe of it
df = pd.DataFrame(raw_df, columns=["date", "title"])
print(df)

# 3. Print all IMAX movie titles with dates of Yongsan CGV
# add `&screencodes=018` to url