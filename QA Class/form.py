import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://demoqa.com/automation-practice-form")
driver.maximize_window()
time.sleep(2)

FirstName=driver.find_element(By.ID,"firstName")
FirstName.send_keys("Manish")
time.sleep(2)

LastName=driver.find_element(By.ID,"lastName")
LastName.send_keys("Tamang")
time.sleep(2)

Email=driver.find_element(By.ID,"userEmail")
Email.send_keys("manish@gmail.com")
time.sleep(2)

Gender=driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div/div[2]/div[2]/form/div[3]/div[2]/div[1]/label")
Gender.click()
time.sleep(2)

MobileNo=driver.find_element(By.ID,"userNumber")
MobileNo.send_keys("9817378027")
time.sleep(2)

Hobbies=driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div/div[2]/div[2]/form/div[7]/div[2]/div[1]/label")
Hobbies.click()
time.sleep(2)

Hobbies=driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div/div[2]/div[2]/form/div[7]/div[2]/div[2]/label")
Hobbies.click()
time.sleep(2)

Hobbies=driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div/div[2]/div[2]/form/div[7]/div[2]/div[3]/label")
Hobbies.click()
time.sleep(2)

Picture=driver.find_element(By.ID,"uploadPicture")
Picture.send_keys("E:/Mardi Trek 2024/MARDI TREK/IMG_1303.JPG")
time.sleep(2)

CurrentAddress=driver.find_element(By.ID,"currentAddress")
CurrentAddress.send_keys("Thankot")
time.sleep(2)

Submit=driver.find_element(By.ID,"submit")
Submit.click()
time.sleep(5)

