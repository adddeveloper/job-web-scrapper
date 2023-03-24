from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import json
import os

filename = os.path.basename(__file__)
url = "https://www.upei.ca/hr/competitions?field_position_type_value=staff"

options = Options()
options.add_argument("--headless")
service = Service("C:/webdrivers/chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)

driver.get(url)
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")
table = soup.find("table", class_="views-table")

arr = []
for tr in table.find_all("tr")[1:]:
    job = tr.find("td", class_="views-field-title").find("a")
    if job:
        title = job.text.strip()
        link = job["href"]
        arr.append({"job": title, "link": link})

print(len(arr))
with open("data/" + filename.split(".")[0] + ".json", "w") as file:
    json.dump(arr, file)

driver.quit()
