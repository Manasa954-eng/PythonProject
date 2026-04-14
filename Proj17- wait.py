import time
from re import findall

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver= webdriver.Chrome()
driver.implicitly_wait(5) #Here the script will wait maxx of 5 secndsin case needed. If the work is done 2 sec, it won't wait another 3 seconds
#Implicit wait is applied globally
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(2)
results = driver.find_elements(By.XPATH, "//div[@class = 'product']")
count = len(results)
assert count > 0

Expected = ["Cucumber - 1 Kg", "Raspberry - 1/4 Kg", "Strawberry - 1/4 Kg" ]
print(Expected)
Actual = driver.find_elements(By.XPATH, "//h4[@class='product-name']")
Actual2 = []

for Real in Actual:
    Actual2.append(Real.text)
print(Actual2)
assert Expected == Actual2

#Chaining- That means the below path will continue from previous path
for result in results:
    result.find_element(By.XPATH, "div/button").click()

driver.find_element(By.XPATH, "(//a/img)[3]").click()
driver.find_element(By.XPATH, "//button[text() = 'PROCEED TO CHECKOUT']").click()


#Sum Validation
prices = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")
sum = 0
for price in prices:
    sum = sum + int(price.text)

Total= driver.find_element(By.CSS_SELECTOR, ".totAmt").text
print(Total)
assert sum == int(Total)



driver.find_element(By.CLASS_NAME, "promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()

#Explicit wait is applied to a particular
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoInfo")))
print(driver.find_element(By.CLASS_NAME, "promoInfo").text)

time.sleep(2)
#Discount is less than Total Amount Validation
discount = driver.find_element(By.CSS_SELECTOR, ".discountAmt").text
print(discount)
assert discount < Total
