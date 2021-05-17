import time
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

EMAIL = "enter your email"
PASSWORD = "enter your password"
job = input("In which you want to do job? \n")
location = input("Enter location where you want to do job:\n")
driver = webdriver.Chrome()
driver.get("https://www.linkedin.com/login")
time.sleep(1)
email = driver.find_element_by_id("username")
email.send_keys(EMAIL)
time.sleep(1)
password = driver.find_element_by_id("password")
password.send_keys(PASSWORD)
time.sleep(1)
sign_in_button = driver.find_element_by_css_selector("form button")
sign_in_button.click()
time.sleep(3)
jobs = driver.find_element_by_id("ember23")
jobs.click()
time.sleep(3)
# all Xpath are taken from CroPath

job_search = driver.find_element(By.XPATH,
                                 "/html[1]/body[1]/div[7]/div[3]/div[1]/section[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/input[1]")
job_search.send_keys(job)
time.sleep(1)
select_city = driver.find_element(By.XPATH,
                                  "/html[1]/body[1]/div[7]/div[3]/div[1]/section[1]/section[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/input[1]")
select_city.send_keys(location)
time.sleep(1)
do_search = driver.find_element(By.XPATH, "/html[1]/body[1]/div[7]/div[3]/div[1]/section[1]/section[1]/div[1]/div[2]/button[1]")
do_search.send_keys(Keys.ENTER)
