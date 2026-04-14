import time

from selenium import webdriver
from selenium.webdriver.common.by import By

name = "Manasa"
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.CSS_SELECTOR, "#name").send_keys(name)
driver.find_element(By.CSS_SELECTOR, "#alertbtn").click()

#The alert that is given is in java. No HTML is written for it. Selenium only automates on HTML, but due to later options we can use 'switch to' to extract such texts
alert = driver.switch_to.alert
alertText = alert.text
print(alertText)

alert.accept()
assert name in alertText










time.sleep(2)