import json
import random
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait



test_path = "C:\\Users\\Manasa\\PycharmProjects\\PythonProject\\Practice\\test_Project.json"
with open(test_path) as b:
    test_data = json.load(b)
    test_data_set = test_data["data"]

@pytest.mark.parametrize("test_one" ,test_data_set)
def test_project(browser, test_one):
    driver = browser

    users = driver.find_element(By.XPATH, "//div[@id='login_credentials']").text

    # username
    user_text = users.split("\n")
    # print(user_text)
    user_text.pop(0)
    # print(user_text)

    username = random.choice(user_text)

    # Password
    passw = driver.find_element(By.CSS_SELECTOR, "div[class='login_password']").text

    password = (passw.split("\n").pop(1))
    assert "secret" in password

    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.CSS_SELECTOR, "input[class='submit-button btn_action']").click()


    prices = driver.find_elements(By.XPATH, "//div[@class='inventory_item_price']")
    target = "$15.99"

    expected_count = 0
    for b in prices:
        if b.text == target:
            expected_count += 1
            # go to parent (inventory_item) and click its button
            b.find_element(By.XPATH, "./ancestor::div[@class='inventory_item']//button").click()

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link")))

#After clicking on the checkout
    driver.find_element(By.CSS_SELECTOR, "a[class='shopping_cart_link']").click()
#Assertion of the items clicked
    cart_items = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
    #Count Validation
    assert len(cart_items) == expected_count
    #Price Validation
    for item in cart_items:
        assert item.text == "$15.99"

    driver.find_element(By.ID, "checkout").click()
    driver.find_element(By.ID, "first-name").send_keys(test_one["firstName"])
    driver.find_element(By.ID, "last-name").send_keys(test_one["lastName"])
    driver.find_element(By.ID, "postal-code").send_keys(test_one["postalCode"])
    driver.find_element(By.ID, "continue").click()
    driver.find_element(By.ID, "finish").click()

    assert "order" in driver.find_element(By.CSS_SELECTOR, "h2").text
