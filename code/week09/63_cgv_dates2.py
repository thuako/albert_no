import requests
from bs4 import BeautifulSoup


url = "http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0191"

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
    print(date_str)
