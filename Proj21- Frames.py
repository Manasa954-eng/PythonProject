import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.implicitly_wait(5)

driver.get("https://the-internet.herokuapp.com/iframe")

wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.frame_to_be_available_and_switch_to_it("mce_0_ifr"))
#Switch to frames that lie on top of html pages to automate them
#driver.switch_to.frame("mce_0_ifr")
driver.find_element(By.CSS_SELECTOR, "#tinymce").clear()
#driver.find_element(By.CSS_SELECTOR, "#tinymce").send_keys(Keys.DELETE)
a = driver.find_element(By.CSS_SELECTOR, "#tinymce").send_keys("Learning")
print(a)
time.sleep(2)
#driver.find_element(By.ID, "tinymce").send_keys("I am able to automate frames")