import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver=webdriver.Chrome()
driver.get("https://demoqa.com/")
driver.maximize_window()
time.sleep(1)

action=ActionChains(driver)
Interactions=driver.find_element(By.XPATH,"//h5[text()='Interactions']")
driver.execute_script("arguments[0].click()",Interactions)
time.sleep(1)

Dragabble=driver.find_element(By.XPATH,"//span[text()='Dragabble']")
driver.execute_script("arguments[0].click()",Dragabble)
time.sleep(1)

Dragme=driver.find_element(By.XPATH,"//div[text()='Drag me']")
action.click_and_hold(Dragme).move_by_offset(100,100).release().perform()
time.sleep(1)

AxisRestricted=driver.find_element(By.XPATH,"//a[text()='Axis Restricted']")
driver.execute_script("arguments[0].click()",AxisRestricted)
time.sleep(1)

OnlyX=driver.find_element(By.XPATH,"//div[text()='Only X']")
action.click_and_hold(OnlyX).move_by_offset(150,0).release().perform()
time.sleep(1)

OnlyY=driver.find_element(By.XPATH,"//div[text()='Only Y']")
action.click_and_hold(OnlyY).move_by_offset(0,150).release().perform()
time.sleep(1)

ContainerRestricted=driver.find_element(By.XPATH,"//a[text()='Container Restricted']")
driver.execute_script("arguments[0].click()",ContainerRestricted)
time.sleep(1)

WithinBox=driver.find_element(By.XPATH,"//div[contains(@class,'draggable ui-widget-content ui-draggable ui-draggable-handle')]")
action.click_and_hold(WithinBox).move_by_offset(200,150).release().perform()
time.sleep(1)

WithinParent=driver.find_element(By.XPATH,"//span[contains(@class,'ui-widget-header ui-draggable ui-draggable-handle')]")
action.click_and_hold(WithinBox).move_by_offset(0,30).release().perform()
time.sleep(1)