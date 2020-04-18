import requests
import time


a = [1, 2, 3]

try:
    print(a[3])
except IndexError:
    print('something is wrong')

i = 100
while i >= 0:
    try:
        print(a[i])
    except IndexError:
        pass
    i = i - 1

url = "http://albert.no.com"
url2 = "http://www.daum.net"
try:
    r = requests.get(url)
    print("success")
except requests.exceptions.RequestException as e:
    print(e)
    r = requests.get(url2)
    print(f"url2 {url2} is requested")

while True:
    time.sleep(1)
    try:
        r = requests.get(url)
        print("success")
    except requests.exceptions.RequestException as e:
        print(e)
