import requests
from bs4 import BeautifulSoup


url = "http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0191"

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

schedule = soup.find('div', class_='item-wrap')

a_list = schedule.find_all('a', href=True)

date_urls = []
for a_item in a_list:
    href_str = a_item['href']
    date_url = "http://www.cgv.co.kr/common/showtimes" + href_str[1:]
    date_urls.append(date_url)
    print(href_str)
print(date_urls)
