from selenium import webdriver
import json
import time
import os
from bs4 import BeautifulSoup

filename = os.path.basename(__file__)

url = 'https://otherocean.com/careers/'
driver = webdriver.Chrome()
driver.get(url)
time.sleep(5)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
tbody = soup.find('tbody', class_='row-hover')
tr = tbody.find_all('tr')

arr = []
for t in tr:
    arrone = {}
    # job title and link
    a = t.find('a')
    if a:
        arrone['job'] = a.text.strip()
        arrone['link'] = 'https:' + a['href']

    # job locations
    location = t.find_all('td', {'class': ['column-2', 'column-3']})
    if location:
        arrone['location'] = [l.text.strip() for l in location]

    # job application link
    apply = t.find('a', href=lambda href: href and "mailto" in href)
    if apply:
        arrone['apply'] = apply['href'].replace('mailto:', '').replace('?Subject=', ' - ')

    if arrone != {}:
        arr.append(arrone)

print(len(arr))
with open("data/"+filename.split('.')[0]+'.json', "w") as file:
    json.dump(arr, file)

driver.quit()
