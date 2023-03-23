from selenium import webdriver
import json
import time
import os
from bs4 import BeautifulSoup

filename = os.path.basename(__file__)

url = 'https://www.maximuscanada.ca/job-postings-charlottetown'
driver = webdriver.Chrome()
driver.get(url)
time.sleep(5)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
anchor = soup.find_all('a', class_='accordion-trigger')


arr = []
for a in anchor:
  arrone = {}
  # heading & anchor

  span = a.find("span")
  if a:
    
    arrone["job"] = span.text

    arrone["link"] = url

  if arrone != {}:
    arr.append(arrone)
    
print(len(arr))
with open("data/"+filename.split('.')[0]+'.json', "w") as file:
    json.dump(arr, file)

driver.quit()