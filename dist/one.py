from selenium import webdriver
import json
import time
import os
from bs4 import BeautifulSoup

filename = os.path.basename(__file__)

url = 'https://workpei.ca/jobs/?job_pei_sector=7326'
driver = webdriver.Chrome()
driver.get(url)
time.sleep(5)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
ul = soup.find('ul', class_='job_listings')
li = ul.find_all("li", class_="job_listing")

arr = []
for l in li:
  arrone = {}
  a = l.find('a', class_='')
  if(a):
    h3 = a.find('h3', class_="job_listing_title")
    if h3:
      arrone["job"] = h3.text
      arrone["link"] = a['href']

  if arrone != {}:
    arr.append(arrone)
    
print(len(arr))
with open("data/"+filename.split('.')[0]+'.json', "w") as file:
    json.dump(arr, file)

driver.quit()