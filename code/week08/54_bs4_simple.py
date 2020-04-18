import requests
from bs4 import BeautifulSoup


url = "http://dataquestio.github.io/web-scraping-pages/simple.html"
page = requests.get(url)

print(page.content)

soup = BeautifulSoup(page.content, 'html.parser')
print(soup.prettify())

p_list = soup.find_all('p')
for p in p_list:
    print(p.get_text())

