import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Firefox()
driver.get("https://demoqa.com/")
driver.maximize_window()

Wait=WebDriverWait(driver,10)

Alerts=Wait.until(EC.element_to_be_clickable((By.XPATH,"//h5[text()='Alerts, Frame & Windows']")))
driver.execute_script("arguments[0].click()",Alerts)

alert=Wait.until(EC.element_to_be_clickable((By.XPATH,"//span[text()='Alerts']")))
driver.execute_script("arguments[0].click()",alert)

clickme=Wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@id='alertButton']")))
driver.execute_script("arguments[0].click()",clickme)

alert1=driver.switch_to.alert
time.sleep(2)
alert1.accept()

confirbox=Wait.until(EC.element_to_be_clickable((By.ID,"confirmButton")))
driver.execute_script("arguments[0].click()",confirbox)

alert2=driver.switch_to.alert
time.sleep(2)
alert2.dismiss()
promptbutton=Wait.until(EC.element_to_be_clickable((By.ID,"promtButton")))
driver.execute_script("arguments[0].click()",promptbutton)

alert3=driver.switch_to.alert
alert3.send_keys("Manish")
time.sleep(2)
print(alert3.text)
alert3.accept()
