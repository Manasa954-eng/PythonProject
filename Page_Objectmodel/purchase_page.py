from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class purchase_screen:
    def __init__(self, driver):
        self.driver = driver
        self.country = (By.ID, "country")
        self.india = (By.LINK_TEXT, "India")
        self.checkbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
        self.success = (By.XPATH, "//input[@class='btn btn-success btn-lg']")
        self.message = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")

    def purchase_me(self, country_name):
        self.driver.find_element(*self.country).send_keys("Ind")
        wait = WebDriverWait(self.driver, 10)

        wait.until(expected_conditions.presence_of_element_located(self.india)).click()
        #self.driver.find_element(*self.india).click()
        self.driver.find_element(*self.checkbox).click()
        self.driver.find_element(*self.success).click()

        message = "Success! Thank you! Your order will be delivered in next few weeks :-)."
        given = self.driver.find_element(*self.message).text
        print(given)
        assert message in given