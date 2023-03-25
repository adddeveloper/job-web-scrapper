from selenium import webdriver
import json
import time
import os
from bs4 import BeautifulSoup

filename = os.path.basename(__file__)

base_url = 'https://emploisfp-psjobs.cfp-psc.gc.ca/psrs-srfp/applicant/page2440?'
params = 'locationsFilter=&selectionProcessNumber=&international=1&title=&search=Search%20jobs&variousLocation=1&officialLanguage=&addedLocation=P6&departments=&log=false'

driver = webdriver.Chrome()
arr = []

driver.get(base_url + params)
time.sleep(5)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

# Find the number of tabs
tab_elems = soup.find_all("li", class_="pagination-page")
num_tabs = len(tab_elems) if tab_elems else 1

# Iterate through each tab
for tab in range(1, num_tabs + 1):
    tab_url = f'{base_url}requestedPage={tab}&fromPage=1&tab=1&log=false'
    driver.get(tab_url)
    time.sleep(5)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    last_page = 1  # default value for the last page number
    last_elem = soup.find("li", class_="last")
    if last_elem:
        last_page = int(last_elem.a["data-page"])

    for page in range(1, last_page + 1):
        # Visit each page
        driver.get(tab_url + f'&page={page}')
        time.sleep(5)
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        li = soup.find_all("li", class_="searchResult")

        for l in li:
            arrone = {}
            a = l.find('a', class_='')
            if a:
                arrone["job"] = a.text
                arrone["link"] = a['href']

            if arrone != {}:
                arr.append(arrone)

print(len(arr))
with open("data/" + filename.split('.')[0] + '.json', "w") as file:
    json.dump(arr, file)

driver.quit()
