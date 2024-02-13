import time
import random
import string
from selenium.common import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Hybrid_test.BaseTest import BaseTest
from Hybrid_test.pages.AccountSuccessPage import AccountSuccessPage
from Hybrid_test.pages.HomePage import HomePage
from Hybrid_test.pages.RegisterPage import RegisterPage
from utilities import ExcelReader
from faker import Faker

fake = Faker()


class TestBoundaryRegister(BaseTest):

    def generate_telephone(self, target_length):
        return ''.join(random.choice('0123456789+-') for _ in range(target_length))

    def extend_length(self, value, target_length):
        while len(value) < target_length:
            value += random.choice(string.ascii_letters)
        return value

    def generate_email(self,email_len):
        random_chars = ''.join(random.choice(string.ascii_letters) for _ in range(email_len - len(fake.email())))
        return random_chars + fake.email()

    def test_boundary_register_warning(self):
        # 从 Excel 读取数据
        data_from_excel = ExcelReader.get_data_from_excel("ExcelFiles/Pairwise.xlsx", "Pairwise")

        for row_data in data_from_excel:
            first_name_len, last_name_len, email_len, telephone_len, password_len = row_data

            # 使用生成的测试数据进行注册
            first_name = self.extend_length(fake.first_name()[:first_name_len], first_name_len)
            last_name = self.extend_length(fake.last_name()[:last_name_len], last_name_len)
            email = self.generate_email(email_len)
            telephone = self.generate_telephone(telephone_len)
            password = self.extend_length(fake.password(length=max(4, password_len)), password_len)  # 最小密码长度为4
            password_confirm = password

            home_page = HomePage(self.driver)
            home_page.click_on_my_account_drop_menu()

            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, home_page.login_option_link_text)))

            home_page.select_register_option()
            register_page = RegisterPage(self.driver)
            register_page.common_register_steps(first_name, last_name, email, telephone, password, password_confirm,
                                                "yes", "select")
            # Check if registration was successful
            try:
                account_success_page = AccountSuccessPage(self.driver)
                account_creation_message = account_success_page.retrieve_account_creation_message()
                if "Your Account Has Been Created!" in account_creation_message:
                    # Registration was successful, now logout
                    home_page.select_logout_option()
                    time.sleep(1)  # Add a small delay to ensure the page updates after logout
            except NoSuchElementException:
                pass  # Account success message not found, continue with checking warnings

    def check_warning_text_for_input(self, input_id, input_value, register_page):
        try:
            # Check if registration was successful
            account_success_page = AccountSuccessPage(self.driver)
            account_creation_message = account_success_page.retrieve_account_creation_message()
            if "Your Account Has Been Created!" in account_creation_message:
                # Registration was successful, no need to check warnings
                return
        except NoSuchElementException:
            pass  # Account success message not found, continue with checking warnings

        # Get the initial number of warning elements
        initial_warnings_count = len(self.driver.find_elements(By.XPATH, "//div[contains(@class, 'warning')]"))

        register_page.enter_input_field_value(input_id, input_value)

        # Wait for a brief moment to ensure the warning elements are updated
        time.sleep(1)

        # Get the updated number of warning elements
        updated_warnings_count = len(self.driver.find_elements(By.XPATH, "//div[contains(@class, 'warning')]"))

        # Check if the number of warning elements increased
        assert updated_warnings_count > initial_warnings_count, f"No warning found for input element: {input_id} with value: {input_value}"
