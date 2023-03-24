from selenium import webdriver
import json
import time
import os
from bs4 import BeautifulSoup

filename = os.path.basename(__file__)

url = 'https://dgi.bamboohr.com/jobs/'
driver = webdriver.Chrome()
driver.get(url)
time.sleep(5)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
div = soup.find('div', class_='ResAts__card')
li = div.find('li')
anchor = li.find_all("a")
def clean(x):
  nx = x.replace("\n", "")
  nx = " ".join(nx.split())
  return nx

arr = []
for a in anchor:
  arrone = {}
  # heading & anchor
  if a:
    arrone["job"] = clean(a.text)
    arrone["link"] = a['href']

  if arrone != {}:
    arr.append(arrone)
    
print(len(arr))
with open("data/"+filename.split('.')[0]+'.json', "w") as file:
    json.dump(arr, file)

driver.quit()