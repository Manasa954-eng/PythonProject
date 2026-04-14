import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class ShopPage:
    def __init__(self, driver):
        self.driver = driver
        self.shop = (By.CSS_SELECTOR, "a[href*='shop']")
        self.card = (By.XPATH, "//div[@class='card h-100']")
        self.checkout = (By.XPATH, "//a[@class='nav-link btn btn-primary']")

    def add_to_cart(self, product_name):
        #wait = WebDriverWait(self.driver, 10)
        #wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "a[href*='shop']"))).click()
        time.sleep(3)
        self.driver.find_element(*self.shop).click()
        options = self.driver.find_elements(*self.card)

        for a in options:
            if a.get_attribute("/div/h4/a") == product_name:
                a.find_element(By.XPATH, "/div/button").click()

    def checkout_button(self):
        self.driver.find_element(*self.checkout).click()