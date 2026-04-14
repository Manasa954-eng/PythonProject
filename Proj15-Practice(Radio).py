import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
radio = driver.find_elements(By.XPATH, "//input[@type='radio']")

for a in radio:
    if a.get_attribute("value") == "radio2":
        a.click()
        assert a.is_selected()
        break

assert driver.find_element(By.ID, "displayed-text").is_displayed()
driver.find_element(By.XPATH, "(//input[@type='submit'])[3]").click()
assert not driver.find_element(By.ID, "displayed-text").is_displayed()



time.sleep(2)
