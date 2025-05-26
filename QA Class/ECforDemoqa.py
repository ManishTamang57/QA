from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Firefox()
driver.get("https://demoqa.com/")
driver.maximize_window()

Wait=WebDriverWait(driver,10)

Forms=Wait.until(EC.element_to_be_clickable((By.XPATH,"//h5[text()='Forms']")))
driver.execute_script("arguments[0].click()",Forms)

PracticeForm=Wait.until(EC.element_to_be_clickable((By.XPATH,"//span[text()='Practice Form']")))
driver.execute_script("arguments[0].click()",PracticeForm)

#Name
FirstName=Wait.until(EC.presence_of_element_located((By.XPATH,"//input[@id='firstName']")))
FirstName.send_keys("Manish")

LastName=Wait.until(EC.presence_of_element_located((By.XPATH,"//input[@id='lastName']")))
LastName.send_keys("Tamang")

#Email
Email=Wait.until(EC.presence_of_element_located((By.XPATH,"//input[@id='userEmail']")))
Email.send_keys("manish@gmail.com")

#Gender
Gender=Wait.until(EC.element_to_be_clickable((By.XPATH,"(//label[contains(@class,'custom-control-label')])[1]")))
driver.execute_script("arguments[0].click()",Gender)

#Mobile Number
MobileNo=Wait.until(EC.presence_of_element_located((By.XPATH,"//input[@id='userNumber']")))
MobileNo.send_keys("9817378027")

#Date of Birth
DOB=Wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@id='dateOfBirthInput']")))
driver.execute_script("arguments[0].click()",DOB)

month=Wait.until(EC.element_to_be_clickable((By.XPATH,"//select[contains(@class,'react-datepicker__month-select')]")))
month.send_keys("October")

year=Wait.until(EC.element_to_be_clickable((By.XPATH,"//select[contains(@class,'react-datepicker__year-select')]")))
year.send_keys("2000")

day=Wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"div.react-datepicker__day--018:not(.react-datepicker__day--outside-month)")))
driver.execute_script("arguments[0].click()",day)

#Subject
Subject=Wait.until(EC.presence_of_element_located((By.XPATH,"//input[@id='subjectsInput']")))
Subject.send_keys("C")

option=Wait.until(EC.element_to_be_clickable((By.XPATH,"//div[text()='Computer Science']")))
driver.execute_script("arguments[0].click()",option)

Subject=Wait.until(EC.presence_of_element_located((By.XPATH,"//input[@id='subjectsInput']")))
Subject.send_keys("M")

option=Wait.until(EC.element_to_be_clickable((By.XPATH,"//div[text()='Maths']")))
driver.execute_script("arguments[0].click()",option)

#Hobbies
Sports=Wait.until(EC.element_to_be_clickable((By.XPATH,"(//label[contains(@class,'custom-control-label')])[4]")))
Reading=Wait.until(EC.element_to_be_clickable((By.XPATH,"(//label[contains(@class,'custom-control-label')])[5]")))
Music=Wait.until(EC.element_to_be_clickable((By.XPATH,"(//label[contains(@class,'custom-control-label')])[6]")))
driver.execute_script("arguments[0].click()",Sports)
driver.execute_script("arguments[0].click()",Reading)
driver.execute_script("arguments[0].click()",Music)

#Picture
Picture=Wait.until(EC.presence_of_element_located((By.ID,"uploadPicture")))
Picture.send_keys(r"E:\Mardi Trek 2024\MARDI TREK\IMG_1303.JPG")

#Address
Address=Wait.until(EC.presence_of_element_located((By.XPATH,"//textarea[@id='currentAddress']")))
Address.send_keys("Thankot")

#State and City
State=Wait.until(EC.element_to_be_clickable((By.ID,"react-select-3-input")))
State.send_keys("H")

Haryana=Wait.until(EC.presence_of_element_located((By.XPATH,"//div[text()='Haryana']")))
driver.execute_script("arguments[0].click()",Haryana)

City=Wait.until(EC.presence_of_element_located((By.ID,"react-select-4-input")))
City.send_keys("P")

Panipat=Wait.until(EC.element_to_be_clickable((By.XPATH,"//div[text()='Panipat']")))
driver.execute_script("arguments[0].click()",Panipat)

#Submit
Submit=Wait.until(EC.element_to_be_clickable((By.ID,"submit")))
driver.execute_script("arguments[0].click()",Submit)