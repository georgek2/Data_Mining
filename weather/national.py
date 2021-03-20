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

print(df)
# 2nd method >> Get individual lists < containers of needed info >
# Loop through the containers
# period_containers = forecast_div.select('.tombstone-container .period-name')

# period_tags = []
# for period in period_containers:
#     name = period.get_text()
#     period_tags.append(name)

# print(period_tags)
# print(len(tombstone_containers))

















