from selenium import webdriver
from selenium.webdriver.common.by import By
#keep it open after the program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

date_list = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
event_list = driver.find_elements(By.CSS_SELECTOR, ".event-widget ul a")
event_dict = {}
for i in range(len(date_list)):
    event_dict[i] = {"date":date_list[i].text, "event":event_list[i].text}

print(event_dict)

driver.quit()