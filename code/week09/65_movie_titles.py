import requests
from bs4 import BeautifulSoup


url = "http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0191"

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

showtimes = soup.find('div', class_='sect-showtimes')

coltimes = showtimes.find_all('div', class_='col-times')

for coltime in coltimes:
    title = coltime.find('a', href=True)
    print(title.get_text())
