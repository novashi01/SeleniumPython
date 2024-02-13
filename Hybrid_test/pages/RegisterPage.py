from selenium.webdriver.common.by import By

from Hybrid_test.pages.BasePage import BasePage


class RegisterPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    first_name_field_id = "input-firstname"
    last_name_field_id = "input-lastname"
    email_field_id = "input-email"
    telephone_field_id = "input-telephone"
    password_field_id = "input-password"
    confirm_field_id = "input-confirm"
    newsletter_field_xpath = "//label[normalize-space()='Yes']//input[@name='newsletter']"
    agree_checkbox_field_name = "agree"
    continue_button_xpath = "//input[@value='Continue']"
    duplicate_email_alert_xpath = "//div[@class='alert alert-danger alert-dismissible']"
    privacy_policy_warning_xpath = '//*[@id="account-register"]/div[1]'
    first_name_warning_xpath = "//input[@id='input-firstname']/following-sibling::div"
    last_name_warning_xpath = "//input[@id='input-lastname']/following-sibling::div"
    email_warning_xpath = "//input[@id='input-email']/following-sibling::div"
    telephone_warning_xpath = "//input[@id='input-telephone']/following-sibling::div"
    password_warning_xpath = "//input[@id='input-password']/following-sibling::div"

    def enter_input_field_value(self, input_id, value):
        print(f"Trying to enter value '{value}' into element with ID '{input_id}'")
        input_element = self.driver.find_element(By.ID, input_id)
        input_element.clear()
        input_element.send_keys(value)

    def enter_first_name(self, first_name_text):
        self.type_into_element(first_name_text,"first_name_field_id", self.first_name_field_id)

    def enter_last_name(self, last_name_text):
        self.type_into_element(last_name_text,"last_name_field_id",self.last_name_field_id)

    def enter_email(self, email_text):
        self.type_into_element(email_text,"email_field_id",self.email_field_id)

    def enter_telephone(self, telephone_text):
        self.type_into_element(telephone_text,"telephone_field_id", self.telephone_field_id)

    def enter_password(self, password_text):
        self.type_into_element(password_text,"password_field_id", self.password_field_id)

    def enter_password_confirm(self, password_text):
        self.type_into_element(password_text,"confirm_field_id", self.confirm_field_id)

    def select_newsletter_field(self):
        self.element_click("newsletter_field_xpath",self.newsletter_field_xpath)

    def select_agree_checkbox_field(self):
        self.element_click("agree_checkbox_field_name",self.agree_checkbox_field_name)

    def click_on_continue_button(self):
        self.element_click("continue_button_xpath",self.continue_button_xpath)

    def common_register_steps(self, first_name, last_name, email, telephone, password, password_confirm, yes_or_no, privacy_policy):
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_email(email)
        self.enter_telephone(telephone)
        self.enter_password(password)
        self.enter_password_confirm(password_confirm)
        if yes_or_no.__eq__("yes"):
            self.select_agree_checkbox_field()
        if privacy_policy.__eq__("select"):
            self.select_newsletter_field()
        return self.click_on_continue_button()

    def retrieve_duplicate_email_alert(self):
        return self.retrieve_element_text("duplicate_email_alert_xpath",self.duplicate_email_alert_xpath)

    def retrieve_privacy_policy_warning(self):
        return self.retrieve_element_text("privacy_policy_warning_xpath",self.privacy_policy_warning_xpath)

    def retrieve_first_name_warning(self):
        return self.retrieve_element_text("first_name_warning_xpath",self.first_name_warning_xpath)

    def retrieve_last_name_warning(self):
        return self.retrieve_element_text("last_name_warning_xpath",self.last_name_warning_xpath)

    def retrieve_email_warning(self):
        return self.retrieve_element_text("email_warning_xpath",self.email_warning_xpath)

    def retrieve_telephone_warning(self):
        return self.retrieve_element_text("telephone_warning_xpath",self.telephone_warning_xpath)

    def retrieve_password_warning(self):
        return self.retrieve_element_text("telephone_warning_xpath",self.password_warning_xpath)