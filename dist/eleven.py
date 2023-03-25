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
divs = soup.find_all("div", class_="faq-box")

arr = []
for div in divs:
    arrone = {}
    h3 = div.find('div', class_='faq-title')
    job = h3.text
    ur = ''
    anchor = div.find_all('a')
    for a in anchor:
        if a.text.lower() == 'apply':
            ur = a['href']
    if job:
        arrone["job"] = job
        arrone["link"] = ur
        arr.append(arrone)

print(len(arr))
with open("data/"+filename.split('.')[0]+'.json', "w") as file:
    json.dump(arr, file)

driver.quit()
