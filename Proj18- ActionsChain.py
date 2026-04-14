import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
action = ActionChains(driver)
action.move_to_element(driver.find_element(By.ID, "mousehover")).perform()
#time.sleep(2)
action.move_to_element(driver.find_element(By.LINK_TEXT, "Reload")).click().perform()
#In this Action chains, perform() at the end is mandatory
