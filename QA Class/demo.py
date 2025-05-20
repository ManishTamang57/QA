import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get("https://demoqa.com/text-box")
driver.maximize_window()
time.sleep(5)
FullName=driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div/div[2]/div[2]/form/div[1]/div[2]/input")
FullName.send_keys("Manish Tamang")
time.sleep(4)
Email=driver.find_element(By. XPATH, "/html/body/div[2]/div/div/div/div[2]/div[2]/form/div[2]/div[2]/input")
Email.send_keys("manish@gmail.com")
time.sleep(4)
CurrentAddress=driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div/div[2]/div[2]/form/div[3]/div[2]/textarea")
CurrentAddress.send_keys("Thankot")
time.sleep(4)
PermanentAddress=driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div/div[2]/div[2]/form/div[4]/div[2]/textarea")
PermanentAddress.send_keys("Udayapur")
time.sleep(4)
Submit=driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div/div[2]/div[2]/form/div[5]/div/button")
Submit.click()
time.sleep(8)