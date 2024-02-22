import requests
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

data = requests.get(url="https://appbrewery.github.io/Zillow-Clone/")
soup =  BeautifulSoup(data.text, "html.parser")
list_price = soup.find_all("span", class_="PropertyCardWrapper__StyledPriceLine")
links = soup.find_all("a", class_="StyledPropertyCardDataArea-anchor")
address = soup.find_all("address")
for i in range(len(list_price)):
    list_price[i] = list_price[i].get_text().replace("/mo", "").split("+")[0]
    links[i] = links[i]['href']
    address[i] = address[i].get_text().strip()

driver = webdriver.Chrome(options=chrome_options)


for i in range(len(list_price)):
    driver.get(url="https://docs.google.com/forms/d/e/1FAIpQLScBIoGxGJGAprJ1WJr60IH-QMLsEQ6tv8G7y5Sj0EU0vm7G1A/viewform?usp=sf_link")
    time.sleep(3)
    add = driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
    add.send_keys(address[i])
    price = driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
    price.send_keys(list_price[i])
    link_form = driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")
    link_form.send_keys(links[i])
    driver.find_element(By.XPATH,"/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div").click()
    time.sleep(2)
