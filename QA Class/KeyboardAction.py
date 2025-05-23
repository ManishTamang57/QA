import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver=webdriver.Firefox()
driver.get("https://demoqa.com/")
driver.maximize_window()
time.sleep(1)

action=ActionChains(driver)

Forms=driver.find_element(By.XPATH,"//h5[text()='Forms']")
driver.execute_script("arguments[0].click()",Forms)
time.sleep(1)

PracticeForm=driver.find_element(By.XPATH,"//span[text()='Practice Form']")
driver.execute_script("arguments[0].click()",PracticeForm)
time.sleep(1)

FirstName=driver.find_element(By.XPATH,"//input[@id='firstName']")
action.click(FirstName).send_keys("Manish"+Keys.ENTER).perform()
time.sleep(1)

LastName=driver.find_element(By.XPATH,"//input[@id='lastName']")
action.click(LastName).send_keys("Tamang"+Keys.TAB).perform()
time.sleep(1)

Email=driver.find_element(By.XPATH,"//input[@id='userEmail']")
action.click(Email).send_keys("manish@gmail.com"+Keys.TAB).perform()
time.sleep(1)

Gender=driver.find_element(By.XPATH,"(//label[contains(@class,'custom-control-label')])[1]")
action.click(Gender).key_down(Keys.TAB).key_up(Keys.TAB).key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()
time.sleep(1)

MobileNo=driver.find_element(By.XPATH,"//input[@id='userNumber']")
action.click(MobileNo).send_keys("9817378027"+Keys.TAB).perform()
time.sleep(1)

Subject=driver.find_element(By.XPATH,"//div[contains(@class,'subjects-auto-complete__value-container subjects-auto-complete__value-container--is-multi css-1hwfws3')]")
action.click(Subject).send_keys("comp").key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).send_keys(Keys.TAB).perform()
time.sleep(1)

Hobbies = driver.find_element(By.XPATH,"//label[@for='hobbies-checkbox-1']")
action.click(Hobbies).perform()

Address=driver.find_element(By.XPATH,"//textarea[@id='currentAddress']")
action.click(Address).send_keys("Thankot"+Keys.TAB).perform()
time.sleep(1)

State=driver.find_element(By.XPATH,"//div[@id='state']")
action.click(State).send_keys("h").send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
time.sleep(5)