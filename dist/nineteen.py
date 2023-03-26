from selenium import webdriver
import json
import time
import os
from bs4 import BeautifulSoup

filename = os.path.basename(__file__)

url = 'https://www.execonline.com/careers/'
driver = webdriver.Chrome()
driver.get(url)
time.sleep(5)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
div = soup.find_all('div', class_='item')

arr = []
for d in div:
  arrone = {}
  # heading & anchor
  a = d.find("a")
  if a:
    arrone["job"] = d.find("h4").text.strip()
    arrone["link"] = a['href']
    arrone["location"] = d.find("div", class_="location").text.strip()
  if arrone != {}:
    arr.append(arrone)

print(len(arr))
with open("data/"+filename.split('.')[0]+'.json', "w") as file:
    json.dump(arr, file)

driver.quit()
