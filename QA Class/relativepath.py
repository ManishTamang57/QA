import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
time.sleep(2)

Username=driver.find_element(By.XPATH,"//input[@name='user-name']")
Username.send_keys("standard_user")
time.sleep(2)

Password=driver.find_element(By.XPATH,"//input[@id='password']")
Password.send_keys("secret_sauce")
time.sleep(2)

Login=driver.find_element(By.XPATH,"//input[@id='login-button']")
Login.click()
time.sleep(2)

AddToCart=driver.find_element(By.XPATH,"//button[contains(@class, 'btn') and contains(@name, 'add-to-cart-sauce-labs-backpack')]")
AddToCart.click()
time.sleep(2)

AddToCart=driver.find_element(By.XPATH,"//button[contains(@class, 'btn') and contains(@name, 'add-to-cart-sauce-labs-bolt-t-shirt')]")
AddToCart.click()
time.sleep(2)

AddToCart=driver.find_element(By.XPATH,"//button[contains(@class, 'btn') and contains(@data-test, 'add-to-cart-sauce-labs-onesie')]")
AddToCart.click()
time.sleep(2)

YourCart=driver.find_element(By.XPATH,"//div[@id='shopping_cart_container']")
YourCart.click()
time.sleep(3)

Remove=driver.find_element(By.XPATH,"//button[contains(@class, 'btn') and contains(@name, 'remove-sauce-labs-onesie')]")
Remove.click()
time.sleep(2)

Checkout=driver.find_element(By.XPATH,"//button[text()='Checkout']")
Checkout.click()
time.sleep(3)

YourInformation=driver.find_element(By.XPATH,"//input[@id='first-name']")
YourInformation.send_keys("Manish")
time.sleep(2)

YourInformation=driver.find_element(By.XPATH,"//input[@id='last-name']")
YourInformation.send_keys("Tamang")
time.sleep(2)

YourInformation=driver.find_element(By.XPATH,"//input[@id='postal-code']")
YourInformation.send_keys("+977")
time.sleep(2)

Continue=driver.find_element(By.XPATH,"//input[@id='continue']")
Continue.click()
time.sleep(2)

Finish=driver.find_element(By.XPATH,"//button[text()='Finish']")
Finish.click()
time.sleep(3)

BackToHome=driver.find_element(By.XPATH,"//button[text()='Back Home']")
BackToHome.click()
time.sleep(5)