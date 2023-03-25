from selenium import webdriver
import json
import time
import os
from bs4 import BeautifulSoup

filename = os.path.basename(__file__)

url = 'https://secure.collage.co/jobs/proserveit'
driver = webdriver.Chrome()
driver.get(url)
time.sleep(5)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
anchor = soup.find_all('a', class_='clearfix')

arr = []
for a in anchor:
    arrone = {}
    div = a.find("div", class_='ATS-position-title')
    if div:
        job_title = div.text.strip().split(' - ')[0]
        arrone["job"] = job_title
    if a.has_attr('href'):
        arrone["link"] = a['href']
    if arrone != {}:
        arr.append(arrone)

print(len(arr))
with open("data/"+filename.split('.')[0]+'.json', "w") as file:
    json.dump(arr, file)

driver.quit()
