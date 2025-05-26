from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.maximize_window()

driver.get("https://demoqa.com/automation-practice-form")
driver.implicitly_wait(5)

subject=driver.find_element(By.XPATH,"//input[@id='subjectsInput']")
subject.send_keys("C")


option=driver.find_element(By.XPATH,"//div[text()='Computer Science']")
driver.execute_script("arguments[0].click()",option)


