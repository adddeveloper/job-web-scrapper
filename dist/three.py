from selenium import webdriver
import time
import json
import os
from bs4 import BeautifulSoup

filename = os.path.basename(__file__)

url = 'https://www.ironfoxgames.com/careers'
driver = webdriver.Chrome()
driver.get(url)
time.sleep(5)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
# title
title = soup.find('title').get_text()
divs = soup.find_all('div', class_='wixui-box')

arr = []

for div in divs:
  arrone = {}
  # h4
  h4 = div.find_all("h4")
  if h4:
    for h in h4:
      span = h.find("span")
      span = span.text
      if span:
        arrone["job"] = span
  # paragraph
  p = div.find("p")
  if p:
    span = p.find("span")
    span = span.text
    if span:
        arrone["discription"]=(span)
  # anchor
  anchor = div.find("a", class_="wixui-button")
  if anchor:
    anchor = anchor['href']
    arrone["link"] = (anchor)
  if arrone != {}:
    arr.append(arrone)

print(len(arr))
with open("data/"+filename.split('.')[0]+'.json', "w") as file:
    json.dump(arr, file)

driver.quit()