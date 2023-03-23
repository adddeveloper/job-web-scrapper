from selenium import webdriver
import json
import time
import os
from bs4 import BeautifulSoup

filename = os.path.basename(__file__)

url = 'https://www.sprypoint.com/pages/careers/current-openings/'
driver = webdriver.Chrome()
driver.get(url)
time.sleep(5)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
li = soup.find_all('li', class_='BambooHR-ATS-Jobs-Item')


arr = []
for l in li:
  arrone = {}
  # heading & anchor

  a = l.find("a")
  if a:
    
    arrone["job"] = a.text

    arrone["link"] = a['href']

  if arrone != {}:
    arr.append(arrone)
    
print(len(arr))
with open("data/"+filename.split('.')[0]+'.json', "w") as file:
    json.dump(arr, file)

driver.quit()