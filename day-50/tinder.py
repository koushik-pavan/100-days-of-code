from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time   #this dumb shit can ruin your life... this is v.v.v.v.v.v.v.v.important for the freaking page to load otherwise it gives NoSuchElement shit..

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://tinder.com/")
time.sleep(2)
sign_in = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a")
sign_in.click()
time.sleep(2)
cookie = driver.find_element(By.XPATH, "/html/body/div[2]/main/div[2]/div/div/div[1]/div[1]/button")
cookie.click()
time.sleep(4)
fb_button = driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button")
fb_button.click()
time.sleep(2)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)
username = driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/form/div/div[1]/div/input")
username.send_keys("koushikvaddadi@gmail.com")
password = driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/form/div/div[2]/div/input")
password.send_keys("beright008@123")
log_in = driver.find_element(By.XPATH,"/html/body/div/div[2]/div[1]/form/div/div[3]/label[2]/input")
log_in.click()
time.sleep(10)
log_in_2 = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div/div/div/div/div[1]/div[3]/div/div/div/div/div/div/div[2]/div/div/div[1]/div/div/div/div[1]/div/div/div/div")
log_in_2.click()
driver.switch_to.window(base_window)
print(driver.title)
time.sleep(10)
location_access = driver.find_element(By.XPATH,"/html/body/div[2]/main/div/div/div/div[3]/button[1]")
location_access.click()
notifications = driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/div/div[3]/button[2]")
notifications.click()
nope = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div/main/div/div/div[1]/div/div[3]/div/div[2]/button")
nope.click()
#driver.quit()