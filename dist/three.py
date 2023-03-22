from selenium import webdriver
import json
import time
import os
from bs4 import BeautifulSoup

filename = os.path.basename(__file__)

url = 'https://www.silverorange.com/job/'
driver = webdriver.Chrome()
driver.get(url)
time.sleep(5)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
# title
title = soup.find('title').get_text()
divs = soup.find_all('div', class_='humi-job-board-posting')

def clean(x):
  nx = x.text.replace("\n", "")
  nx = " ".join(nx.split())
  return nx


arr = []
for div in divs:
  arrone = {}
  # heading & anchor
  a = div.find("a")
  if a:
    
    arrone["job"] = a.text

    arrone["link"] = a['href']
  # paragrahp
  d = div.find("div", class_="humi-job-board-posting-details")
  if d:
    arrone["discription"] = clean(d)
  if arrone != {}:
    arr.append(arrone)

# print(arr, len(arr))
with open("data/"+filename.split('.')[0]+'.json', "w") as file:
    json.dump(arr, file)

driver.quit()