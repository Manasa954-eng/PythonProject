import random
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-notifications")
chrome_options.add_experimental_option("prefs", {
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False,
    "profile.password_manager_leak_detection": False
})
chrome_options.add_argument("--disable-features=PasswordLeakDetection")

driver = webdriver.Chrome(options = chrome_options)
driver.implicitly_wait(2)

driver.get("https://www.saucedemo.com/")
users = driver.find_element(By.XPATH, "//div[@id='login_credentials']" ).text

#username
user_text  = users.split("\n")
print(user_text)
user_text.pop(0)
print(user_text)

username = random.choice(user_text)

#Password
passw = driver.find_element(By.CSS_SELECTOR, "div[class='login_password']").text

password = (passw.split("\n").pop(1))
print(password)


driver.find_element(By.ID, "user-name").send_keys(username)
driver.find_element(By.ID, "password").send_keys(password)
driver.find_element(By.CSS_SELECTOR, "input[class='submit-button btn_action']").click()

driver.implicitly_wait(5)

price = driver.find_elements(By.XPATH, "//div[@class='pricebar']")

for a in price:
    if a.find_element(By.XPATH, "//div[@class='pricebar']/div") == "$15.99":
        a.find_element(By.XPATH, "//div[@class='pricebar']/button").click()

driver.find_element(By.CSS_SELECTOR, "a[class='shopping_cart_link']").click()
driver.find_element(By.ID, "checkout").click()
driver.find_element(By.ID, "first-name").send_keys("Manasa")
driver.find_element(By.ID, "last-name").send_keys("Veerabomma")
driver.find_element(By.ID, "postal-code").send_keys("500034")
driver.find_element(By.ID, "continue").click()
driver.find_element(By.ID, "finish").click()
assert "order" in driver.find_element(By.CSS_SELECTOR, "h2").text
