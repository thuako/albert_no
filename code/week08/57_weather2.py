import requests
from bs4 import BeautifulSoup


page = requests.get("http://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168")
soup = BeautifulSoup(page.content, 'html.parser')

seven_day = soup.find(id="seven-day-forecast-container")

period_tags = seven_day.select(".tombstone-container .period-name")
periods = []
for pt in period_tags:
    periods.append(pt.get_text())

#periods = [pt.get_text() for pt in period_tags]
print(periods)

short_descs = [sd.get_text() for sd in seven_day.select(".tombstone-container .short-desc")]
temps = [t.get_text() for t in seven_day.select(".tombstone-container .temp")]
descs = [d["title"] for d in seven_day.select(".tombstone-container img")]
print(short_descs)
print(temps)
print(descs)
