import time
from datetime import datetime
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from Hybrid_test.pages.AccountSuccessPage import AccountSuccessPage
from Hybrid_test.pages.HomePage import HomePage
from Hybrid_test.pages.RegisterPage import RegisterPage
from Hybrid_test.conftest import handle_possible_element_not_found,check_element_exists
from Hybrid_test.BaseTest import BaseTest


class TestRegister(BaseTest):

    def test_register_with_mandatory_field(self):
        home_page = HomePage(self.driver)
        home_page.click_on_my_account_drop_menu()
        home_page.select_register_option()
        register_page = RegisterPage(self.driver)
        register_page.enter_first_name("test")
        register_page.enter_last_name("03")
        register_page.enter_email(TestRegister.generate_email_with_time_stamp())
        register_page.enter_telephone("12345678")
        register_page.enter_password("Test123456")
        register_page.enter_password_confirm("Test123456")
        register_page.select_newsletter_field()
        register_page.select_agree_checkbox_field()
        register_page.click_on_continue_button()
        expected_heading_text = "Your Account Has Been Created!"
        account_success_page = AccountSuccessPage(self.driver)
        assert account_success_page.retrieve_account_creation_message().__eq__(expected_heading_text)

    def test_register_with_duplicate_email(self):
        home_page = HomePage(self.driver)
        home_page.click_on_my_account_drop_menu()
        home_page.select_register_option()
        register_page = RegisterPage(self.driver)
        register_page.enter_first_name("test")
        register_page.enter_last_name("03")
        register_page.enter_email("test02@test.co")
        register_page.enter_telephone("12345678")
        register_page.enter_password("Test123456")
        register_page.enter_password_confirm("Test123456")
        register_page.select_newsletter_field()
        register_page.select_agree_checkbox_field()
        register_page.click_on_continue_button()
        expected_alerting_text = "Warning: E-Mail Address is already registered!"
        assert register_page.retrieve_duplicate_email_alert().__eq__(
            expected_alerting_text)

    def test_register_without_entering_any_fields(self):
        home_page = HomePage(self.driver)
        home_page.click_on_my_account_drop_menu()
        home_page.select_register_option()
        register_page = RegisterPage(self.driver)
        register_page.enter_first_name("")
        register_page.enter_last_name("")
        register_page.enter_email("")
        register_page.enter_telephone("")
        register_page.enter_password("")
        register_page.enter_password_confirm("")
        register_page.select_newsletter_field()
        # register_page.select_agree_checkbox_field() # Don't agree that!!! There is no Warning!!!
        register_page.click_on_continue_button()
        # time.sleep(3)
        expected_alerting_text = "Warning: You must agree to the Privacy Policy!"
        assert register_page.retrieve_privacy_policy_warning().__contains__(
            expected_alerting_text)
        expected_01_warning_text = "First Name must be between 1 and 32 characters!"
        assert self.driver.find_element(By.XPATH, "//input[@id='input-firstname']/following-sibling::div").text.__eq__(
            expected_01_warning_text)
        expected_02_warning_text = "Last Name must be between 1 and 32 characters!"
        assert self.driver.find_element(By.XPATH, "//input[@id='input-lastname']/following-sibling::div").text.__eq__(
            expected_02_warning_text)
        expected_03_warning_text = "E-Mail Address does not appear to be valid!"
        assert self.driver.find_element(By.XPATH, "//input[@id='input-email']/following-sibling::div").text.__eq__(
            expected_03_warning_text)
        expected_04_warning_text = "Telephone must be between 3 and 32 characters!"
        assert self.driver.find_element(By.XPATH, "//input[@id='input-telephone']/following-sibling::div").text.__eq__(
            expected_04_warning_text)
        expected_05_warning_text = "Password must be between 4 and 20 characters!"
        assert self.driver.find_element(By.XPATH, "//input[@id='input-password']/following-sibling::div").text.__eq__(
            expected_05_warning_text)



