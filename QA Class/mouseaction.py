import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver=webdriver.Chrome()
driver.get("https://demoqa.com/")
driver.maximize_window()

action=ActionChains(driver)
Elements=driver.find_element(By.XPATH,"//h5[text()='Elements']")
driver.execute_script("arguments[0].click()",Elements)
time.sleep(2)

elements=driver.find_element(By.XPATH,"//div[text()='Elements']")
driver.execute_script("arguments[0].click()",elements)
time.sleep(2)

Buttons=driver.find_element(By.XPATH,"//span[text()='Buttons']")
driver.execute_script("arguments[0].click()",Buttons)
time.sleep(2)

DoubleClick=driver.find_element(By.XPATH,"//button[text()='Double Click Me']")
action.double_click(DoubleClick).perform()
time.sleep(2)

RightClick=driver.find_element(By.XPATH,"//button[@id='rightClickBtn']")
action.context_click(RightClick).perform()
time.sleep(2)

Clickme=driver.find_element(By.XPATH,"//button[text()='Click Me']")
driver.execute_script("arguments[0].click()",Clickme)
time.sleep(2)