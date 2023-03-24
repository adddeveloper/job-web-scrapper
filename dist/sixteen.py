from selenium import webdriver
import json
import time
import os
from bs4 import BeautifulSoup

filename = os.path.basename(__file__)

url = 'https://staygolden.ca/page/careers'
driver = webdriver.Chrome()
driver.get(url)
time.sleep(5)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
cards = soup.find_all('div', class_='Item__Card-sc-e6zi9i-0')

arr = []
for card in cards:
  arrone = {}
  
  title = card.find('div', class_='TitleBlock__Title-sc-psm0fl-4')
  if title:
    arrone['job'] = title.text
    
  company = card.find('div', class_='TitleBlock__InfoItem-sc-psm0fl-5', recursive=False)
  if company:
    arrone['company'] = company.text
    
  location = card.find_all('div', class_='TitleBlock__InfoItem-sc-psm0fl-5')[2]
  if location:
    arrone['location'] = location.text
    
  arrone['link'] = url

  if arrone != {}:
    arr.append(arrone)

print(len(arr))
with open("data/"+filename.split('.')[0]+'.json', "w") as file:
    json.dump(arr, file)

driver.quit()
