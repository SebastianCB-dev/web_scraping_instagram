#Libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, urllib.request
import requests

# Credentials
from credentials import getPassword, getUsername

#Chrome Web Driver
PATH = "/home/sebastiancb/Downloads/chromedriver"
driver = webdriver.Chrome(PATH)

# Open Instagram URL
driver.get("https://www.instagram.com/")

# Screen Login Instagram
time.sleep(5)
username_input = driver.find_element_by_css_selector("input[name='username']")
password_input = driver.find_element_by_css_selector("input[name='password']")
username_input.clear()
password_input.clear()
username_input.send_keys(getUsername())
password_input.send_keys(getPassword())
time.sleep(5)
login = driver.find_element_by_css_selector("button[type='submit']").click()
time.sleep(20)

# Screen Save your login info
login_save_info_button_not_now = driver.find_element_by_xpath("//button[contains(text(), 'Not now')]").click()
time.sleep(10)

# Screen Turn On Notifications
turn_on_notificacion_not_not_button = driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
time.sleep(10)

# Search person 
input_search = driver.find_element_by_css_selector("input[type=text]")
input_search.clear()
input_search.send_keys("Chelsea F.C.")
time.sleep(5)
# Double enter to confirm
input_search.send_keys(Keys.ENTER)
input_search.send_keys(Keys.ENTER)
time.sleep(1000)