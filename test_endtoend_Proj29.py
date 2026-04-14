import json
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Page_Objectmodel.checkout_page import checkout_screen
from Page_Objectmodel.login import LoginPage
from Page_Objectmodel.purchase_page import purchase_screen
from Page_Objectmodel.shop import ShopPage

#accessing from the json file
test_path = 'C:\\Users\\Manasa\\PycharmProjects\\PythonProject\\data\\test_endnote_Proj29.json'
with open(test_path) as f: #reading the json file and feeding it to the current file as f
    test_data = json.load(f) #reading that f file, which is fed
    test_list = test_data["data"] #accessing the read file information


@pytest.mark.parametrize("test_list_one", test_list) #Accessing the separate data of the json file bu using test_list_one (some random name)
def test_complete(browserInstance, test_list_one):
    driver = browserInstance
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    login = LoginPage(driver)  #object name is login
    print(login.getTitle())
    login.login(test_list_one["userName"], test_list_one["userPassword"])

    shop = ShopPage(driver)
    shop.add_to_cart(test_list_one["productName"])
    shop.checkout_button()

    hit_one = checkout_screen(driver)
    hit_one.hit()

    purchase_one = purchase_screen(driver)
    purchase_one.purchase_me("India")
