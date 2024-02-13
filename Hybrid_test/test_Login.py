import time
import pytest
import os
import pandas as pd
from datetime import datetime
from selenium import webdriver
from utilities import ReadConfigurations, ExcelViodReader
from Hybrid_test.pages.AccountPage import AccountPage
from Hybrid_test.pages.HomePage import HomePage
from Hybrid_test.pages.LoginPage import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Hybrid_test.BaseTest import BaseTest

class TestLogin(BaseTest):

    @pytest.mark.parametrize("email,password", ExcelViodReader.get_data_from_excel(
        "ExcelFiles/login_test_data.xlsx", "LoginTest"))
    def test_login_invalid_problem(self, email, password):
        home_page = HomePage(self.driver)
        home_page.click_on_my_account_drop_menu()

        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, home_page.login_option_link_text)))

        home_page.select_login_option()
        login_page = LoginPage(self.driver)

        if email and password is not None:
            login_page.enter_password(password)

        if password is not None:
            login_page.enter_password(password)

        if email is not None:
            login_page.enter_email_address(email)

        # if it is a def code
        if email == "generate_email_with_time_stamp()":
            login_page.enter_email_address(TestLogin.generate_email_with_time_stamp())

        time.sleep(1)
        login_page.click_on_login_button()
        time.sleep(1)

        account_page = AccountPage(self.driver)
        actual_warning_message = account_page.retrieve_warning_message()

        expected_warning_messages = [
            "Warning: No match for E-Mail Address and/or Password.",
            "Warning: Your account has exceeded allowed number of login attempts. Please try again in 1 hour.",
            # 添加其他可能的警告消息
        ]

        assert any(expected_message in actual_warning_message for expected_message in
                   expected_warning_messages), f"Actual message: {actual_warning_message}"

    def test_login_with_valid_email_and_valid_password(self):
        home_page = HomePage(self.driver)
        home_page.click_on_my_account_drop_menu()

        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, home_page.login_option_link_text)))

        home_page.select_login_option()
        login_page = LoginPage(self.driver)
        login_page.enter_email_address("test02@test.co")
        login_page.enter_password("12345678")
        time.sleep(2)
        login_page.click_on_login_button()

        account_page = AccountPage(self.driver)
        assert account_page.display_status_of_edit_account_option()