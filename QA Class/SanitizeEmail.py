import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Firefox()
driver.get("https://sanitize-crm.netlify.app/login")
driver.maximize_window()
Wait=WebDriverWait(driver,10)

Email=Wait.until(EC.presence_of_element_located((By.NAME,"email")))
Email.send_keys("tmgmanish57@gmail.com")
time.sleep(1)

Password=Wait.until(EC.presence_of_element_located((By.NAME,"password")))
Password.send_keys("P@ssw0rd")
time.sleep(1)

RememberMe=Wait.until(EC.element_to_be_clickable((By.XPATH,"//label[text()='Remember Me']")))
RememberMe.click()
time.sleep(1)

Login=Wait.until(EC.element_to_be_clickable((By.XPATH,"//button[text()='Login']")))
Login.click()
time.sleep(1)

UpgradePlan=Wait.until(EC.element_to_be_clickable((By.XPATH,"//button[text()='Upgrade Plan']")))
UpgradePlan.click()
time.sleep(1)

UpgradetoPro=Wait.until(EC.element_to_be_clickable((By.XPATH,"(//button[text()='Upgrade to '])[1]")))
UpgradetoPro.click()
time.sleep(1)

Upgrade=Wait.until(EC.element_to_be_clickable((By.XPATH,"//button[text()='Upgrade']")))
Upgrade.click()
time.sleep(1)

driver.switch_to.frame("paddle_frame")

Checkbox=Wait.until(EC.element_to_be_clickable((By.XPATH,"//div[contains(@class,'checkbox')]")))
Checkbox.click()
time.sleep(1)

Continue=Wait.until(EC.element_to_be_clickable((By.XPATH,"//button[text()='Continue']")))
Continue.click()
time.sleep(1)

CardNo=Wait.until(EC.presence_of_element_located((By.ID,"cardNumber")))
CardNo.send_keys("4111111111111111")
time.sleep(1)

NameonCard=Wait.until(EC.presence_of_element_located((By.ID,"cardHolder")))
NameonCard.send_keys("Test")
time.sleep(1)

ExpiryDate=Wait.until(EC.presence_of_element_located((By.NAME,"expiry")))
ExpiryDate.send_keys("1226")
time.sleep(1)

SecurityCode=Wait.until(EC.presence_of_element_located((By.ID,"cvv")))
SecurityCode.send_keys("123")
time.sleep(1)

Subscribe=Wait.until(EC.element_to_be_clickable((By.XPATH,"//button[text()='Subscribe now']")))
Subscribe.click()
time.sleep(1)

