import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver=webdriver.Firefox()
driver.get("https://demoqa.com/")
driver.maximize_window()
time.sleep(2)

action=ActionChains(driver)
Interactions=driver.find_element(By.XPATH,"//h5[text()='Interactions']")
driver.execute_script("arguments[0].click()",Interactions)
time.sleep(2)

Droppable=driver.find_element(By.XPATH,"//span[text()='Droppable']")
driver.execute_script("arguments[0].click()",Droppable)
time.sleep(2)

Drag_me=driver.find_element(By.XPATH,"//div[@id='draggable']")
Drop_here=driver.find_element(By.XPATH,"(//div[contains(@class,'drop-box ui-droppable')])[1]")
action.drag_and_drop(Drag_me,Drop_here).release().perform()
time.sleep(2)

Accept=driver.find_element(By.XPATH,"//a[text()='Accept']")
driver.execute_script("arguments[0].click()",Accept)
time.sleep(2)

NotAcceptable=driver.find_element(By.XPATH,"//div[text()='Not  Acceptable']")
Drophere=driver.find_element(By.XPATH,"(//div[contains(@class,'drop-box ui-droppable')])[2]")
action.drag_and_drop(NotAcceptable,Drophere).release().perform()
time.sleep(2)
action.click_and_hold(NotAcceptable).move_by_offset(-200, -60).release().perform()
time.sleep(2)

Acceptable=driver.find_element(By.XPATH,"//div[text()='Acceptable']")
Drophere=driver.find_element(By.XPATH,"(//div[contains(@class,'drop-box ui-droppable')])[2]")
action.drag_and_drop(Acceptable,Drophere).release().perform()
time.sleep(2)

Prevent_Propagation=driver.find_element(By.XPATH,"//a[text()='Prevent Propogation']")
driver.execute_script("arguments[0].click()",Prevent_Propagation)
time.sleep(2)

dragme=driver.find_element(By.XPATH,"//div[text()='Drag Me']")
UpperDroppable=driver.find_element(By.XPATH,"//div[@id='notGreedyInnerDropBox']")
action.drag_and_drop(dragme,UpperDroppable).release().perform()
time.sleep(2)

dragme=driver.find_element(By.XPATH,"//div[text()='Drag Me']")
LowerInDroppable=driver.find_element(By.XPATH,"//div[@id='greedyDropBoxInner']")
action.drag_and_drop(dragme,LowerInDroppable).release().perform()
time.sleep(2)

action.click_and_hold(dragme).move_by_offset(0,-108).release().perform() #to move up i.e. to outter droppable
time.sleep(2)

RevertDraggable=driver.find_element(By.XPATH,"//a[text()='Revert Draggable']")
driver.execute_script("arguments[0].click()",RevertDraggable)
time.sleep(2)

WillRevert=driver.find_element(By.XPATH,"//div[text()='Will Revert']")
Drophere=driver.find_element(By.XPATH,"(//div[@id='droppable'])[3]")
action.drag_and_drop(WillRevert,Drophere).release().perform()
time.sleep(2)

NotRevert=driver.find_element(By.XPATH,"//div[@id='notRevertable']")
Drophere=driver.find_element(By.XPATH,"(//div[@id='droppable'])[3]")
action.drag_and_drop(NotRevert,Drophere).release().perform()
time.sleep(2)