from selenium.webdriver.common.by import By
from faker import Faker
import random

fake = Faker()


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def type_into_element(self, text, locator_name, locator_value):
        element = self.get_element(locator_name, locator_value)
        element.click()
        element.clear()
        element.send_keys(text)

    def element_click(self, locator_name, locator_value):
        element = self.get_element(locator_name, locator_value)
        element.is_displayed()
        element.click()

    def check_display_status_of_element(self,locator_name, locator_value):
        element = self.get_element(locator_name, locator_value)
        return element.is_displayed()

    def retrieve_element_text(self,locator_name, locator_value):
        element = self.get_element(locator_name, locator_value)
        return element.text

    def get_element(self, locator_name, locator_value):
        element = None
        if locator_name.endswith("_id"):
            element = self.driver.find_element(By.ID, locator_value)
        elif locator_name.endswith("_name"):
            element = self.driver.find_element(By.NAME, locator_value)
        elif locator_name.endswith("_class"):
            element = self.driver.find_element(By.CLASS_NAME, locator_value)
        elif locator_name.endswith("_link_text"):
            element = self.driver.find_element(By.LINK_TEXT, locator_value)
        elif locator_name.endswith("_xpath"):
            element = self.driver.find_element(By.XPATH, locator_value)
        elif locator_name.endswith("_css"):
            element = self.driver.find_element(By.CSS_SELECTOR, locator_value)
        elif locator_name.endswith("_tag_name"):
            element = self.driver.find_element(By.TAG_NAME, locator_value)
        return element

    def generate_data_with_lengths(self, first_name_len, last_name_len, email_len, telephone_len, password_len):
        data = {
            'first_name': fake.first_name()[:first_name_len],
            'last_name': fake.last_name()[:last_name_len],
            'email': fake.email()[:email_len],
            'telephone': fake.phone_number()[:telephone_len],
            'password': fake.password(length=password_len)
        }
        return data

