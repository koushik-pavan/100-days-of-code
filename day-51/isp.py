from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

PROMISED_DOWN = 150
PROMISED_UP = 10

class InternetSpeedTwitterBot:
    def __init__(self, up, down):
        self.driver = webdriver.Chrome(options=chrome_options)
        self.down = down
        self.up = up

    def get_internet_speed(self):
        self.driver.get(url="https://www.speedtest.net/")
        time.sleep(2)
        cookie = self.driver.find_element(By.XPATH, "/html/body/div[5]/div[2]/div/div/div[2]/div[1]/div/button")
        cookie.click()
        time.sleep(2)
        go_button = self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a")
        go_button.click()
        time.sleep(30)
        download_speed = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
        download_speed = download_speed.text
        upload_speed = self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span")
        upload_speed = upload_speed.text
        self.down = download_speed
        self.up = upload_speed
        self.driver.quit()

    def tweet_at_provider(self):
        self.driver.get(url="https://twitter.com/")
        time.sleep(5)
        log_in = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[5]/a')
        log_in.click()
        time.sleep(10)

        input_no = self.driver.find_element(By.NAME, "text")
        input_no.send_keys("8248298176")
        input_no.send_keys(Keys.ENTER)
        time.sleep(5)
        password = self.driver.find_element(By.NAME, "password")
        password.send_keys("beright008@123")
        password.send_keys(Keys.ENTER)
        time.sleep(6)
        tweet_compose = self.driver.find_element(By.CLASS_NAME, 'public-DraftStyleDefault-ltr')
        tweet = (f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for "
                 f"{PROMISED_DOWN}down/{PROMISED_UP}up?")
        tweet_compose.send_keys(tweet)
        time.sleep(3)
        #click on post button after this if you want to post


my_speed = InternetSpeedTwitterBot(0,0)
my_speed.get_internet_speed()
my_speed.tweet_at_provider()