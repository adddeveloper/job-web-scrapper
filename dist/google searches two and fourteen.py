from selenium import webdriver
from selenium.webdriver.common.by import By
import json
import time
import os
from bs4 import BeautifulSoup
import string
import unicodedata

filename = os.path.basename(__file__)

urls = [    'https://www.google.com/search?q=it+jobs&ibp=htl;jobs&sa=X&ved=2ahUKEwjj0t_og_P9AhXgFVkFHZMvAzAQutcGKAF6BAgKEAU&sxsrf=AJOqlzUSaKYRr4-4XMSomZ3q3BDCyvz-ZQ:1679608115626#htivrt=jobs&htidocid=6D6zNQ2RW58AAAAAAAAAAA%3D%3D&fpstate=tldetail',    'https://www.google.com/search?q=paytic+jobs&oq=paytic+jobs&aqs=chrome..69i57.1366j0j1&sourceid=chrome&ie=UTF-8&ibp=htl;jobs&sa=X&ved=2ahUKEwjqpLCn0J39AhXlD1kFHRpSAMcQkd0GegQIFRAB#fpstate=tldetail&htivrt=jobs&htiq=paytic+jobs&htidocid=O5m_KDAblCMAAAAAAAAAAA%3D%3D&sxsrf=AJOqlzUCzUUQ5S5cL7IaApyWCpY7VsgmVA:1676673710569']

driver = webdriver.Chrome()
arr = []
for url in urls:
    driver.get(url)
    time.sleep(5)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    lis = soup.find_all('li', class_='iFjolb')

    for li in lis:
        arrone = {}
        h2 = li.find('div', class_='Fol1qc')
        anchor = li.find_all("a")
        # an = soup.find("pMhGee")
        if h2:
            arrone["job"] = h2.text
        if anchor:
            for a in anchor:
                if a.text.split(' ')[0] == "Apply":
                    arrone["link"] = a['href']
        if 'link' not in arrone.keys():
            print('')
            anc = soup.find('div', {'id':'tl_ditsc'}).find("div", class_="pE8vnd").find_all('a')
            for an in anc:
                if an.text.split(' ')[0] == "Apply":
                    arrone["link"] = an['href']
                    print(an)
        if arrone != {}:
            arr.append(arrone)

print(len(arr))
with open("data/"+filename.split('.')[0]+'.json', "w") as file:
    json.dump(arr, file)

driver.quit()
