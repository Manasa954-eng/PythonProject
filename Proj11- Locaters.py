import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.CSS_SELECTOR, "input[name = 'name']").send_keys("Manasa")
driver.find_element(By.NAME, "email").send_keys("abc.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("Manasa@21")

#Static Drop-down
dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropdown.select_by_index(1)
#dropdown.select_by_visible_text("Female")  #Other ways
driver.find_element(By.CSS_SELECTOR, "#inlineRadio2").click()
driver.find_element(By.ID, "exampleCheck1").click()
driver.find_element(By.XPATH, "//input[@type = 'submit']").click()
message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)
assert "Success" in message

#CSS Selector-- #id, .class, tagname[attribute= 'Value], parent child:nth-child(index) child

#X Path-- //tagname[@attribute = 'Value'],//parent/child[index]/child, To create a X Path based on a given text--> //tagname[text() = 'Text of the locator']


time.sleep(2)
