import pandas as pd
import requests
from bs4 import BeautifulSoup


# url = "http://ee.hongik.ac.kr/dept/ee/0301.html"
url = "http://www.hongik.ac.kr/front/boardlist.do?bbsConfigFK=78&siteGubun=1&menuGubun=1"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

# QUIZ: create a dataframe with "name", "url", "email", "webpage" of professors

# Question 1: loop on dataframe
# Question 2: Exeptions (prof. Jongsun Kim)
# hint: href["href"]

subject_list = soup.find_all('div', class_="subject")

names = [subject.find('span').get_text() for subject in subject_list]
url_list = [subject.find('a')['href'] for subject in subject_list]

email_list = []
webpage_list = []
hongik_url = "http://www.hongik.ac.kr"

for url in url_list:
    row_page = requests.get(hongik_url+url)
    row_soup = BeautifulSoup(row_page.content, 'html.parser')
    substance = row_soup.find('div', class_='substance')
    href_list = substance.find_all('a', href=True)
    substance_email = ''
    substance_webpage = ''
    for href in href_list:
        href_text = href['href']
        if ('mailto' in href_text) and (len(substance_email) <= len(href_text[7:])):
            substance_email = href_text[7:]
        if ('http://' in href_text) and (len(substance_webpage) <= len(href_text)):
            substance_webpage = href_text
    email_list.append(substance_email)
    webpage_list.append(substance_webpage)

df = pd.DataFrame({
    "name": names,
    "url": url_list,
    "email": email_list,
    "webpage": webpage_list,
})
for i in range(9):
    print(df.iloc[i])
