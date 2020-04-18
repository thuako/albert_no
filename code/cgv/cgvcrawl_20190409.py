import re
import requests
from bs4 import BeautifulSoup


url_head = "https://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01"

theater = 13  # yongsan I-park
url_theater = f"&theaterCode={theater:04d}"

screen_num = 18  # IMAX
url_screen = f"&screencodes={screen_num:03d}"

url_all = url_head + url_theater + url_screen
print(url_all)

page = requests.get(url_all)
soup = BeautifulSoup(page.content, "html.parser")

### extract dates
showtimes = soup.find(class_='showtimes-wrap')
sect_schedule = showtimes.find(class_='sect-schedule')
slider = sect_schedule.find(id='slider')
dates = slider.find_all('a')
for date in dates:
    date_str = date.get('href')
    date_idx = date_str.find('date=')
    print(date_str[date_idx+5:date_idx+13])
    #print(date.get_text().split())
#
# ### extract movies
# date = "20190410"
# url_date = f"&date={date}"
# url_with_date = url_all + url_date
# page = requests.get(url_with_date)
# soup = BeautifulSoup(page.content, "html.parser")
#
# showtimes = soup.find(class_='showtimes-wrap')
# sect_showtimes = showtimes.find(class_='sect-showtimes')
# col_times = sect_showtimes.find_all(class_='col-times')
#
# # print(sect_showtimes)
# for col_time in col_times:
#     info_movie = col_time.find(class_='info-movie')
#     title = info_movie.find('a').get_text().strip()
#     type_halls = col_time.find_all(class_='type-hall')
#     for type_hall in type_halls:
#         info_hall = type_hall.find(class_='info-hall')
#         screen_types = info_hall.find_all('li')
#         print(f"title = {title} type = {screen_types[1].get_text().strip()}")
#
# # TBD: make it as pandas dataframe


