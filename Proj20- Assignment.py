import time
from unittest import expectedFailure

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.find_element(By.LINK_TEXT, "Free Access to InterviewQues/ResumeAssistance/Material").click()
time.sleep(2)

WindowOpened = driver.window_handles
driver.switch_to.window(WindowOpened[1])
time.sleep(2)

username = driver.find_element(By.CSS_SELECTOR, "div p:nth-child(2)").text
print(username)
a = (username.split("at")[1])
print(a.split()[0])

driver.switch_to.window(WindowOpened[0])
driver.find_element(By.CSS_SELECTOR, "#username").send_keys(a)
driver.find_element(By.ID, "password").send_keys("Learning@830$3mK2")
driver.find_element(By.ID, "signInBtn").click()
time.sleep(1)
#print(driver.page_source)

wait = WebDriverWait(driver, 10)
error = wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".alert")))
print(error.text)