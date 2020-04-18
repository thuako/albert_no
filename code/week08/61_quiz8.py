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
