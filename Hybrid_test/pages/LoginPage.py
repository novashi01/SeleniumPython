from selenium.webdriver.common.by import By

from Hybrid_test.pages.AccountPage import AccountPage
from Hybrid_test.pages.BasePage import BasePage


class LoginPage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)

    email_address_field_id = "input-email"
    password_field_id = "input-password"
    login_button_xpath = "//input[@value='Login']"
    warning_message_xpath = "//div[@class='alert alert-danger alert-dismissible']"

    def enter_email_address(self,email_address_text):
        self.type_into_element(email_address_text,"email_address_field_id",self.email_address_field_id)

    def enter_password(self,password_text):
        self.type_into_element(password_text,"password_field_id",self.password_field_id)

    def click_on_login_button(self):
        self.element_click("login_button_xpath",self.login_button_xpath)

    def login_to_application(self,email_address_text,password_text):
        self.enter_email_address(email_address_text)
        self.enter_password(password_text)
        if self.click_on_login_button():
            return AccountPage(self.driver)
        else:
            return None

    def retrieve_warning_message(self):
        return self.retrieve_element_text("warning_message_xpath",self.warning_message_xpath)



