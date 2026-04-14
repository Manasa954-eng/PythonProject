import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

def test_complete(browserInstance):
    driver = browserInstance
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    driver.find_element(By.ID, "username").send_keys("rahulshettyacademy")
    driver.find_element(By.ID, "password").send_keys("Learning@830$3mK2")
    driver.find_element(By.ID, "signInBtn").click()



    driver.implicitly_wait(5)

    driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
    options = driver.find_elements(By.XPATH, "//div[@class='card h-100']")

    for a in options:
        if a.get_attribute("/div/h4/a") == "Blackberry":
            a.find_element(By.XPATH, "/div/button").click()

    driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").click()
    driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
    driver.find_element(By.ID, "country").send_keys("Ind")
    wait = WebDriverWait(driver, 10)

    wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
    driver.find_element(By.LINK_TEXT, "India").click()
    driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
    driver.find_element(By.XPATH, "//input[@class='btn btn-success btn-lg']").click()

    message = "Success! Thank you! Your order will be delivered in next few weeks :-)."
    given = driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text
    print(given)
    assert message in given

