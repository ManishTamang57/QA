import time

from selenium import webdriver
driver= webdriver.Edge()
driver.get("https://authorized-partner.netlify.app/register/")
driver.maximize_window()
time.sleep(5)