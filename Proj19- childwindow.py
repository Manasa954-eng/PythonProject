import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)

driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.LINK_TEXT, "Click Here").click()
WindowsOpened = driver.window_handles
time.sleep(3)
driver.switch_to.window(WindowsOpened[1])
print(driver.find_element(By.TAG_NAME, "h3").text)
driver.close()

driver.switch_to.window(WindowsOpened[0])
assert "Opening a new window" == driver.find_element(By.TAG_NAME, "h3").text