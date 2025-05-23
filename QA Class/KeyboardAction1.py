import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver=webdriver.Firefox()
driver.maximize_window()

driver.get("https://authorized-partner.netlify.app/register/")

action=ActionChains(driver)

Checkbox=driver.find_element(By.XPATH,"//button[@id='remember']")
driver.execute_script("arguments[0].click()",Checkbox)
time.sleep(1)
#action.send_keys(Keys.TAB).send_keys(Keys.TAB).send_keys(Keys.TAB).perform()

Continue=driver.find_element(By.XPATH,"//button[text()='Continue']")
driver.execute_script("arguments[0].click()",Continue)
time.sleep(1)


FirstName=driver.find_element(By.XPATH,"//input[contains(@placeholder,'Enter Your First Name')]") #for first name
action.click(FirstName).send_keys("Manish").send_keys(Keys.ENTER).perform()
time.sleep(1)


action.send_keys("Tamang").send_keys(Keys.TAB).perform() #for last name
time.sleep(1)


action.send_keys("manish@gmail.com").send_keys(Keys.TAB).perform() #for email
time.sleep(1)


action.send_keys("9817378027").send_keys(Keys.TAB).perform() #for phone number
time.sleep(1)


action.send_keys(Keys.TAB).send_keys("P@ssw0rd").send_keys(Keys.TAB).perform() #for password
time.sleep(1)


action.send_keys(Keys.TAB).send_keys("P@ssw0rd").send_keys(Keys.TAB).perform() #confirm password
time.sleep(1)


action.send_keys(Keys.TAB).send_keys(Keys.ENTER).perform() #for next button
