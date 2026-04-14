import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.mark.smoke
def test_sort(browserInstance):
    driver = browserInstance
    #driver = webdriver.Chrome()
    #driver.implicitly_wait(5)

    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

    Sortedelements = []

    driver.find_element(By.XPATH, "//span[text() = 'Veg/fruit name']").click()

    time.sleep(2)

    Sortedwebelements = driver.find_elements(By.XPATH, "//tr/td[1]")

    for ele in Sortedwebelements:
        Sortedelements.append(ele.text)

    Originalelements = Sortedelements.copy()

    Sortedelements.sort()

    assert Originalelements == Sortedelements
