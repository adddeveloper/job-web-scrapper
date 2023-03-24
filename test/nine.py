from selenium import webdriver
import json
import time
import os
from bs4 import BeautifulSoup
from urllib.parse import urljoin

filename = os.path.basename(__file__)

url = 'https://harriscomputer.wd3.myworkdayjobs.com/en-US/1?locations=d853aaf7f8c7105815543438235211df'
driver = webdriver.Chrome()
driver.get(url)
time.sleep(5)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
div = soup.find('div', class_='css-uvpbop')
ul = div.find('ul')

li = ul.find_all("li")

def clean(x):
  nx = x.replace("\n", "")
  nx = " ".join(nx.split())
  return nx

arr = []
for l in li:
  arrone = {}
  # heading & anchor
  a = l.find("a")

  if a:
    arrone["job"] = clean(a.text)
    print(str(a['href']).split(':')[0])
    if(str(a['href']).split(':')[0] != 'https' and str(a['href']).split(':')[0] != 'http'):
      ur = urljoin(url,a['href'])
      arrone["link"] = ur
    else:
      arrone["link"] = a['href']
  if arrone != {}:
    arr.append(arrone)
    
print(len(arr))
with open("data/"+filename.split('.')[0]+'.json', "w") as file:
    json.dump(arr, file)

driver.quit()