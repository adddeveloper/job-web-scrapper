from selenium import webdriver
from bs4 import BeautifulSoup
import json
import os

# Set up file path and website URL
filename = os.path.basename(__file__)
url = 'https://hollandcollege.com/about/Careers.php'

# Open the website using selenium
driver = webdriver.Chrome()
driver.get(url)

# Get the page source and parse it using BeautifulSoup
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

# Find the table containing job listings
table = soup.find('table')

# Find all the rows in the table except the last one
rows = table.find_all('tr')[:-1]

# Create an empty list to store job data
jobs = []

# Loop through each row and extract job name and link
for row in rows:
    cols = row.find_all('td')
    if cols:
        job = cols[0].find('a').text.strip()
        link = cols[0].find('a')['href']
        jobs.append({
            'job': job,
            'link': link
        })

# Print the number of jobs found and close the browser
print(f"Number of jobs found: {len(jobs)}")
driver.quit()

# Write the job data to a JSON file
with open("data/" + filename.split('.')[0] + '.json', "w") as file:
    json.dump(jobs, file)
