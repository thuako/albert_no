import pandas as pd
import requests
from bs4 import BeautifulSoup


# url = "http://ee.hongik.ac.kr/dept/ee/0301.html"
url = "http://www.hongik.ac.kr/front/boardlist.do?bbsConfigFK=78&siteGubun=1&menuGubun=1"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
#print(soup)

subject_list = soup.find_all('div', class_="subject")
for subject in subject_list:
    name = subject.find('span').get_text()

names = [subject.find('span').get_text() for subject in subject_list]
url_list = [subject.find('a')['href'] for subject in subject_list]
print(names)
print(url_list)

df = pd.DataFrame({
    "name": names,
    "url": url_list,
})
print(df)


