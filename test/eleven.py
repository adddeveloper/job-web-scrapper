from selenium import webdriver
import json
import time
import os
from bs4 import BeautifulSoup

filename = os.path.basename(__file__)

url = 'https://www.stemble.com/stemble-careers'
driver = webdriver.Chrome()
driver.get(url)
time.sleep(5)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
divs = soup.find_all('div', class_='faq-title')

arr = []
for div in divs:
    arrone = {}
    # heading
    job = div.text.strip()
    if job:
        arrone["job"] = job
        arrone["link"] = url
        arr.append(arrone)

print(len(arr))
with open("data/"+filename.split('.')[0]+'.json', "w") as file:
    json.dump(arr, file)

driver.quit()
