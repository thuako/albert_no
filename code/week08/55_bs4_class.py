import requests
from bs4 import BeautifulSoup


url = "http://dataquestio.github.io/web-scraping-pages/ids_and_classes.html"
page = requests.get(url)

#print(page.content)

soup = BeautifulSoup(page.content, 'html.parser')
#print(soup.prettify())

p_list = soup.find_all('p')
# for p in p_list:
#     print(p.get_text())

p_outer_list = soup.find_all('p',  class_='outer-text')
for p_outer in p_outer_list:
    print(p_outer.get_text())

p_first_list = soup.find_all('p', id='first')
for p_first in p_first_list:
    print(p_first.get_text())
