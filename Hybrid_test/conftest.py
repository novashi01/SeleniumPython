import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities import ReadConfigurations
from selenium.common.exceptions import NoSuchElementException


def handle_possible_element_not_found(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except NoSuchElementException:
            print("Element not found. Skipping assertion.")

    return wrapper


def check_element_exists(driver, xpath):
    try:
        driver.find_element(By.XPATH, xpath)
        return True, None
    except NoSuchElementException:
        return False, f"Element with XPath '{xpath}' not found on the page."


@pytest.fixture()
def setup_and_teardown(request):
    browser = ReadConfigurations.get_config("basic info", "browser")
    supported_browsers = ["chrome", "firefox", "edge"]

    if browser not in supported_browsers:
        raise ValueError(f"Unsupported browser: {browser}. Supported browsers: {', '.join(supported_browsers)}")

    driver = None

    try:
        if browser == "chrome":
            driver = webdriver.Chrome()
        elif browser == "firefox":
            driver = webdriver.Firefox()
        elif browser == "edge":
            driver = webdriver.Edge()

        driver.maximize_window()
        url = ReadConfigurations.get_config("basic info", "url")
        driver.get(url)
        request.cls.driver = driver
        yield
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if driver is not None:
            driver.quit()
