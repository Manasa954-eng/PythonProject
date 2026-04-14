import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://sauce-demo.myshopify.com/account/register")
driver.find_element(By.XPATH, "//input[@id='first_name']").send_keys("Manasa")
driver.find_element(By.XPATH, "//input[@id = 'last_name']").send_keys("Veerabomma")
driver.find_element(By.XPATH, "//form/div[4]/input").send_keys("manasa.veerabomma2000@gmail.com")
driver.find_element(By.CSS_SELECTOR, "form div:nth-child(7) input").send_keys("Manasa@21")

wait = WebDriverWait(driver, 10)
create_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input[value='Create']" )) ).click()
#driver.find_element(By.CSS_SELECTOR, "input[value='Create']").click()
#driver.implicitly_wait(10)
print("Before Click")
driver.execute_script("arguments[0].click();", create_btn)
time.sleep(5)
#driver.find_element(By.LINK_TEXT, "reset your password").click()
