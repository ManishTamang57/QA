
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Firefox()
driver.get("https://demoqa.com/")
driver.maximize_window()

Wait=WebDriverWait(driver,10)

Widgets=Wait.until(EC.element_to_be_clickable((By.XPATH,"//h5[text()='Widgets']")))
driver.execute_script("arguments[0].click()",Widgets)

DatePicker=Wait.until(EC.element_to_be_clickable((By.XPATH,"//span[text()='Date Picker']")))
driver.execute_script("arguments[0].click()",DatePicker)

SelectDate=Wait.until(EC.element_to_be_clickable((By.ID,"datePickerMonthYearInput")))
driver.execute_script("arguments[0].click()",SelectDate)

month=Wait.until(EC.element_to_be_clickable((By.XPATH,"//select[contains(@class,'react-datepicker__month-select')]")))
month.send_keys("October")

year=Wait.until(EC.element_to_be_clickable((By.XPATH,"//select[contains(@class,'react-datepicker__year-select')]")))
year.send_keys("2000")

day=Wait.until(EC.element_to_be_clickable((By.XPATH,"//div[contains(@class,'react-datepicker__day') and text()='18']")))
driver.execute_script("arguments[0].click()",day)

#Date and Time
DateandTime=Wait.until(EC.element_to_be_clickable((By.ID,"dateAndTimePickerInput")))
driver.execute_script("arguments[0].click()",DateandTime)

month1=Wait.until(EC.element_to_be_clickable((By.XPATH,"//div[contains(@class,'react-datepicker__month-read-view')]")))
driver.execute_script("arguments[0].click()",month1)

July=Wait.until(EC.element_to_be_clickable((By.XPATH,"//div[text()='July']")))
driver.execute_script("arguments[0].click()",July)

year1=Wait.until(EC.element_to_be_clickable((By.XPATH,"//div[contains(@class,'react-datepicker__year-read-view')]")))
driver.execute_script("arguments[0].click()",year1)

year_select=Wait.until(EC.element_to_be_clickable((By.XPATH,"//div[text()='2022']")))
driver.execute_script("arguments[0].click()",year_select)

day=Wait.until(EC.element_to_be_clickable((By.XPATH,"//div[contains(@class,'react-datepicker__day') and text()='18']")))
driver.execute_script("arguments[0].click()",day)

#time
time_select=Wait.until(EC.element_to_be_clickable((By.XPATH,"//li[text()='14:45']")))
driver.execute_script("arguments[0].click()",time_select)
