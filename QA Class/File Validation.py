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
time.sleep(2)

VerifyEmail=Wait.until(EC.element_to_be_clickable((By.XPATH,"//div[text()='Verify Email']")))
driver.execute_script("arguments[0].click()",VerifyEmail)
time.sleep(2)

FileValidation=Wait.until(EC.element_to_be_clickable((By.XPATH,"//div[text()='File Validation']")))
driver.execute_script("arguments[0].click()",FileValidation)
time.sleep(1)

UploadFile=Wait.until(EC.element_to_be_clickable((By.XPATH,"//button[span[text()='Upload File']]")))
driver.execute_script("arguments[0].click()",UploadFile)
time.sleep(1)

ListName=Wait.until(EC.presence_of_element_located((By.XPATH,"//input[@placeholder='List Name']")))
ListName.send_keys("Test")
time.sleep(1)

FileUpload=Wait.until(EC.presence_of_element_located((By.XPATH,"//input[@type='file']")))
FileUpload.send_keys(r"C:\Users\User\OneDrive\Desktop\DOC\emails.csv")
time.sleep(1)

ValidationType= Wait.until(EC.presence_of_element_located((By.XPATH,"//div[@class='basic-multi-select css-b62m3t-container']")))
ValidationType.click()
ValidationOption= Wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'select__option') and contains(., 'SMTP validation')]")))
driver.execute_script("arguments[0].click()",ValidationOption)
ValidationOption.click()

RunValidation=Wait.until(EC.element_to_be_clickable((By.XPATH,"//button[text()='Run Validation']")))
driver.execute_script("arguments[0].click()",RunValidation)


