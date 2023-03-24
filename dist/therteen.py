from selenium import webdriver
import json
import time
import os
from bs4 import BeautifulSoup

filename = os.path.basename(__file__)

urls = [    'https://emploisfp-psjobs.cfp-psc.gc.ca/psrs-srfp/applicant/page2440?locationsFilter=&selectionProcessNumber=&international=1&title=&search=Search%20jobs&variousLocation=1&officialLanguage=&addedLocation=P6&departments=&log=false',    'https://emploisfp-psjobs.cfp-psc.gc.ca/psrs-srfp/applicant/page2440?requestedPage=2&fromPage=1&tab=1&log=false']

driver = webdriver.Chrome()
arr = []
for url in urls:
    driver.get(url)
    time.sleep(5)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    last_page = 1  # default value for the last page number
    last_elem = soup.find("li", class_="last")
    if last_elem:
        last_page = int(last_elem.a["data-page"])

    for page in range(1, last_page + 1):
        # Visit each page
        driver.get(url + f'&page={page}')
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
with open("data/"+filename.split('.')[0]+'.json', "w") as file:
    json.dump(arr, file)

driver.quit()
