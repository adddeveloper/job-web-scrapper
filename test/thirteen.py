from selenium import webdriver
import json
import time
import os
from bs4 import BeautifulSoup
from urllib.parse import urljoin

filename = os.path.basename(__file__)

base_url = 'https://emploisfp-psjobs.cfp-psc.gc.ca/psrs-srfp/applicant/page2440?'
params = 'locationsFilter=&selectionProcessNumber=&international=1&title=&tab=1&search=Search%20jobs&variousLocation=1&officialLanguage=&addedLocation=P6&departments=&log=false'

driver = webdriver.Chrome()
arr = []

driver.get(base_url + params)
time.sleep(20)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

# Find the number of pages
page_links = soup.find("span", class_="pagelinks")
if page_links:
    num_pages = max(int(x) for x in page_links.text.split() if x.isdigit())
else:
    num_pages = 1

# Iterate through each page
for page in range(1, num_pages + 1):
    page_url = f'{base_url}requestedPage={page}&fromPage=1&tab=1&log=false'
    driver.get(page_url)
    time.sleep(5)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    li = soup.find_all("li", class_="searchResult")

    for l in li:
        arrone = {}
        a = l.find('a', class_='')
        if a:
            arrone["job"] = a.text
            if(str(a['href']).split(':')[0] != 'https' and str(a['href']).split(':')[0] != 'http'):
                ur = urljoin(base_url, a['href'])
                arrone["link"] = ur
            else:
                arrone["link"] = a['href']

        if arrone != {}:
            arr.append(arrone)

print(len(arr))
with open("data/" + filename.split('.')[0] + '.json', "w") as file:
    json.dump(arr, file)

driver.quit()
