import pandas as pd
import requests
from bs4 import BeautifulSoup


# url = "http://ee.hongik.ac.kr/dept/ee/0301.html"
url = "http://www.hongik.ac.kr/front/boardlist.do?bbsConfigFK=78&siteGubun=1&menuGubun=1"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

subject_list = soup.find_all('div', class_="subject")

names = [subject.find('span').get_text() for subject in subject_list]
url_list = [subject.find('a')['href'] for subject in subject_list]
print(names)
print(url_list)

df = pd.DataFrame({
    "name": names,
    "url": url_list,
})

hongik_url = "http://www.hongik.ac.kr"

row_page = requests.get(hongik_url+url_list[0])
row_soup = BeautifulSoup(row_page.content, 'html.parser')
substance = row_soup.find('div', class_='substance')
href_list = substance.find_all('a', href=True)
for href in href_list:
    href_text = href.get_text()
    if '@' in href_text:
        print(f"email : {href_text}")
    else:
        print(f"webpage: {href_text}")



