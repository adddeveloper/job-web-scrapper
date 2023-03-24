from selenium import webdriver
import json
import time
import os
from bs4 import BeautifulSoup

filename = os.path.basename(__file__)

url = 'https://sculpinqa.com/career/'
driver = webdriver.Chrome()
driver.get(url)
time.sleep(5)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
tbody = soup.find('tbody')
tr = tbody.find_all('tr')

arr = []
for t in tr:
  arrone = {}
  a = t.find("a")
  if a:
    arrone["job"] = a.text
    arrone["link"] = a['href']
    arrone["location"] = t.find_all("td")[2].text
    
  if arrone != {}:
    arr.append(arrone)

print(len(arr))
with open("data/"+filename.split('.')[0]+'.json', "w") as file:
    json.dump(arr, file)

driver.quit()
