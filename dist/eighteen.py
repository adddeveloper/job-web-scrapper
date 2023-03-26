from selenium import webdriver
from bs4 import BeautifulSoup
import json
import os

filename = os.path.basename(__file__)
url = 'https://hollandcollege.com/about/Careers.php'

driver = webdriver.Chrome()
driver.get(url)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

table = soup.find('table')

rows = table.find_all('tr')[:-1]

jobs = []

for row in rows:
    cols = row.find_all('td')
    if cols:
        job = cols[0].find('a').text.strip()
        link = cols[0].find('a')['href']
        jobs.append({
            'job': job,
            'link': link
        })

print(f"Number of jobs found: {len(jobs)}")
driver.quit()

with open("data/" + filename.split('.')[0] + '.json', "w") as file:
    json.dump(jobs, file)
