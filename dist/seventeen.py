from selenium import webdriver
from bs4 import BeautifulSoup
import json
import os
from urllib.parse import urljoin

filename = os.path.basename(__file__)
url = "https://www.upei.ca/hr/competitions?field_position_type_value=staff"
driver = webdriver.Chrome()
driver.get(url)
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")
table = soup.find("table", class_="views-table")

arr = []
for tr in table.find_all("tr")[1:]:
    job = tr.find("td", class_="views-field-title").find("a")
    if job:
        title = job.text.strip()
        if(str(job['href']).split(':')[0] != 'https' and str(job['href']).split(':')[0] != 'http'):
            ur = urljoin(url,job['href'])
            link = ur
        else:
            link = job['href']
        arr.append({"job": title, "link": link})

print(len(arr))
with open("data/" + filename.split(".")[0] + ".json", "w") as file:
    json.dump(arr, file)

driver.quit()
