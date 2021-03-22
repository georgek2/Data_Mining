import requests 
from bs4 import BeautifulSoup as soup 

import pandas as pd

page = requests.get('https://forecast.weather.gov/MapClick.php?lat=64.80808789800005&lon=-151.00415781499996#.YFXx9Ggza00')

print(page.status_code)
page_soup = soup(page.content, 'html.parser')

forecast_div = page_soup.find(id='seven-day-forecast-container')


# print(forecast_div.prettify())

## 1st method >> CSS selectors & List Comprehensions
## Easy

period_names = [period.get_text() for period in forecast_div.select('.tombstone-container .period-name')]
period_desc = [period.get_text() for period in forecast_div.select('.tombstone-container .short-desc')]
period_details = [detail.img['title'] for detail in forecast_div.select('.tombstone-container')]

# print(period_names)
# print(period_desc)
# print(period_details)

df = pd.DataFrame({'Period': period_names, 'Description': period_desc, 'Details': period_details})

# print(df)


# 2nd method >> Using bs4 find elements
# >> Get individual lists < containers of needed info >
# Loop through the containers
# period_containers = forecast_div.select('.tombstone-container .period-name')

period_containers = forecast_div.find_all(class_='period-name')
period_tags = []

for period in period_containers:
    name = period.get_text()
    period_tags.append(name)

# print(period_tags)
# print(len(tombstone_containers))

verdict_containers = forecast_div.findAll(class_='short-desc')
verdicts = []

for v in verdict_containers:
    verdict = v.get_text()
    verdicts.append(verdict)


print(verdicts)

period_descs = forecast_div.findAll(class_='tombstone-container')
descs = []

for period in period_descs:
    d = period.img['title']
    descs.append(d)

# print(descs)

# Write to a csv file
file = 'file.csv'
headers = 'Period, Verdict, Description\n' # CSV headers

with open(file, 'a') as f:
    f.write(headers)
for period, verdict, desc in zip(period_tags, verdicts, descs): 
    with open(file, 'a') as f:
        f.write(period + ',' + verdict + ',' + desc)


with open(file, 'r') as f:
    content = f.read()

print(content)






