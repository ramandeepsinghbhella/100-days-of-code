from selenium import webdriver
from selenium.webdriver.common.by import By
import time

EMAIL = "enter your email"
PASSWORD = "enter your password"
PROMISED_DOWN = 150
PROMISED_UP = 10


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.down = 0
        self.up = 0

    def getInternetSpeed(self):
        site = self.driver.get("https://www.speedtest.net/")
        go = self.driver.find_element_by_css_selector("a .start-text")
        go.click()
        time.sleep(45)
        download_speed = self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        self.down = download_speed.text
        upload_speed = self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span')
        self.up = upload_speed.text

    def tweeterAtProvider(self):

        site = self.driver.get("https://twitter.com/LOGIN")
        time.sleep(1)
        email = self.driver.find_element(By.NAME, "session[username_or_email]").send_keys(EMAIL)
        time.sleep(1)
        password = self.driver.find_element(By.NAME, "session[password]")
        password.send_keys(PASSWORD)
        sign_in = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div')
        sign_in.click()
        time.sleep(5)
        tweet_compose = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')

        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        tweet_compose.send_keys(tweet)
        time.sleep(3)

        tweet_button = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]')
        tweet_button.click()

        time.sleep(2)
        self.driver.quit()

bot = InternetSpeedTwitterBot()
bot.getInternetSpeed()
bot.tweeterAtProvider()
