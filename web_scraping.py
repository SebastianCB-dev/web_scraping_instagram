#Libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, urllib.request
import requests

# Credentials
from credentials import getPassword, getUsername

#Chrome Web Driver
PATH = "C:\\Users\\SebastianCB-dev\\Downloads\\chromedriver_win32\\chromedriver.exe"
driver = webdriver.Chrome(PATH)

# Open Instagram URL
driver.get("https://www.instagram.com/")

# Screen Login Instagram
time.sleep(5)
username = driver.find_element_by_css_selector("input[name='username']")
password = driver.find_element_by_css_selector("input[name='password']")
username.clear()
password.clear()
username.send_keys(getUsername())
password.send_keys(getPassword())
time.sleep(5)
login = driver.find_element_by_css_selector("button[type='submit']").click()
time.sleep(20)