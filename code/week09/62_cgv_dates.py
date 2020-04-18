import requests
from bs4 import BeautifulSoup


# http://www.cgv.co.kr/reserve/show-times/?areacode=01&theaterCode=0191&date=20190503
# ifrm_movie_time_table
url = "http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0191&date=20190503"
# NOTE: it has date information already

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

schedule = soup.find('div', class_='item-wrap')
#print(schedule)

a_list = schedule.find_all('a', href=True)
for a_item in a_list:
    print(a_item.get_text())

for idx, a_item in enumerate(a_list):
    print(idx, a_item.get_text().split())
    print(idx, a_item['href'])
