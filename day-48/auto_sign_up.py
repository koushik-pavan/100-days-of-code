from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("http://secure-retreat-92358.herokuapp.com/")

driver.find_element(By.NAME, "fName").send_keys("pavan")
driver.find_element(By.NAME, "lName").send_keys("pavan")
driver.find_element(By.NAME, "email").send_keys("pavan@gmail.com")
driver.find_element(By.CLASS_NAME, "btn").click()
#driver.quit()