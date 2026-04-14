import pytest
from selenium import webdriver




def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="Browser options"
    )


@pytest.fixture()
def browser(request):

    browser_name = request.config.getoption("browser_name")

    if browser_name == "chrome":
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_experimental_option("prefs", {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.password_manager_leak_detection": False
        })
        chrome_options.add_argument("--disable-features=PasswordLeakDetection")
        driver = webdriver.Chrome(options=chrome_options)

    elif browser_name == "firefox":
        driver = webdriver.Firefox()

    elif browser_name == "edge":
        driver = webdriver.Edge()

    else:
        raise Exception("Driver not supported")

    driver.implicitly_wait(5)

    driver.get("https://www.saucedemo.com/")

    yield driver
    driver.quit()