import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Firefox()
driver.maximize_window()
driver.get("https://training.rcvacademy.com/test-automation-practice-page")

#using select_by_visible_text()
Dropdown=Select(driver.find_element(By.XPATH,"//select[contains(@class,'form-control zen-custom-elm')]"))
Dropdown.select_by_visible_text("Google")
time.sleep(2)

#For another option using select_by_index()
dropdown=driver.find_element(By.XPATH,"//select[contains(@class,'form-control zen-custom-elm')]")
select=Select(dropdown)
select.select_by_index(1)
time.sleep(2)

#Another option using select_by_visible_text()
option=Select(driver.find_element(By.XPATH,"//select[contains(@class,'form-control zen-custom-elm')]"))
option.select_by_visible_text("Meta")
time.sleep(2)

#Again using select_by_index()
nextoption=driver.find_element(By.XPATH,"//select[contains(@class,'form-control zen-custom-elm')]")
Amazon=Select(nextoption)
Amazon.select_by_index(4)

