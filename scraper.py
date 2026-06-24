import requests 
from bs4 import BeautifulSoup
from selenium import webdriver
import time 
def get_emploi():
    data=[]
    driver = webdriver.Chrome()

    driver.get("https://remoteok.com/remote-python-jobs")

    time.sleep(5)

    print(driver.title)
    soup= BeautifulSoup(
        driver.page_source,
        "html.parser"
    )
    jobs= soup.find_all("tr", class_="job")
    for job in jobs:
        titre= job.find("h2", itemprop= "title").text.strip()
        entreprise= job.find("h3", itemprop= "name").text.strip()
        lien="https://remoteok.com" + job.find("a", class_= "preventLink")["href"]
        id= job["data-id"]
        data.append({
            "titre" : titre,
            "entreprise" : entreprise,
            "lien": lien,
            "id": id
        })
        
    
    print(len(jobs))
    return data
