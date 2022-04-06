from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, urllib.request
import requests

PATH = "C:\\Users\\SebastianCB-dev\\Downloads\\chromedriver_win32\\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.instagram.com/")

#login
time.sleep(5)
username = driver.find_element_by_css_selector("input[name='username']")
password = driver.find_element_by_css_selector("input[name='password']")
username.clear()
password.clear()
username.send_keys("Input User")
password.send_keys("password")
time.sleep(1000)
