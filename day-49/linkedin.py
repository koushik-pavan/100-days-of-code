from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time   #this dumb shit can ruin your life... this is v.v.v.v.v.v.v.v.important for the freaking page to load otherwise it gives NoSuchElement shit..

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3829363473&keywords=python%20developer&origin=JOBS_HOME_KEYWORD_AUTOCOMPLETE&refresh=true")
driver.find_element(By.LINK_TEXT, "Sign in").click()
driver.find_element(By.ID, "username").send_keys("pavankoushik2023@gmail.com")
password_field = driver.find_element(By.ID, "password")
password_field.send_keys("beright008@123")
password_field.send_keys(Keys.ENTER)

list=[]
list = driver.find_elements(By.CSS_SELECTOR, '.job-card-container__link')
print(len(list))
for i in list:
    i.click()
    time.sleep(3)
    print(i.text)
    try:
        apply_button = driver.find_element(By.CSS_SELECTOR, "button.jobs-save-button")
        apply_button.click()
        time.sleep(3)
    except:
        print("No application button, skipped.")
    else:
        continue
#print(text)
#driver.quit()