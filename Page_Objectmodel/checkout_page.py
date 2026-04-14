import pytest
from selenium.webdriver.common.by import By

class checkout_screen:
    def __init__(self, driver):
        self.driver = driver
        self.press = (By.XPATH, "//button[@class='btn btn-success']")

    def hit(self):
        self.driver.find_element(*self.press).click()


