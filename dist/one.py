from selenium import webdriver
import json
import time
import os
from bs4 import BeautifulSoup

filename = os.path.basename(__file__)

def save_deleted_data(existing_data, new_data, deleted_data_file):
    # Compare the existing data and new data, creating a list of deleted_data.
    # If a job in existing_data is not present in the new_data, it will be added to the deleted_data list.
    deleted_data = [job for job in existing_data if job not in new_data]
    
    # If there are any items in the deleted_data list, save them to the deleted_data_file.
    if deleted_data:
        with open(deleted_data_file, "w") as file:
            json.dump(deleted_data, file, indent=2)



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

existing_data_file = "data/{}.json".format(filename)
deleted_data_file = "deleteddata/{}.json".format(filename)

if os.path.exists(existing_data_file):
    with open(existing_data_file, "r") as file:
        existing_data = json.load(file)
else:
    existing_data = []

save_deleted_data(existing_data, arr, deleted_data_file)

with open("data/"+filename.split('.')[0]+'.json', "w") as file:
    json.dump(arr, file)

driver.quit()