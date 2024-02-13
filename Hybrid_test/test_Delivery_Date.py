import time
from datetime import datetime
import pytest
from selenium.webdriver.common.by import By
from Hybrid_test.pages.CheckOutPage import CheckOutPage
from Hybrid_test.pages.HomePage import HomePage
from Hybrid_test.pages.ProductPage import ProductPage
from Hybrid_test.pages.SearchPage import SearchPage
from Hybrid_test.BaseTest import BaseTest


expected_text = "Your order has been placed!"


class TestDeliveryDate(BaseTest):

    def print_red(text1, text2):
        print("\033[91m{}\033[0m".format(text1, text2))

    def test_product_delivery_date(self):
        try:
            # Define the target date
            expected_date = "2024-02-29"
            expected_date = datetime.strptime(expected_date, "%Y-%m-%d")

            # Define month_number dictionary
            month_number = {
                "January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6,
                "July": 7, "August": 8, "September": 9, "October": 10, "November": 11, "December": 12
            }

            home_page = HomePage(self.driver)
            home_page.common_login()
            time.sleep(1)
            home_page.enter_product_into_search_box_field("HP")
            home_page.click_on_search_button()
            search_page = SearchPage(self.driver)
            search_page.display_status_of_product()
            search_page.click_valid_product()
            time.sleep(3)
            product_page = ProductPage(self.driver)
            current_month_text = product_page.retrieve_current_month_year()
            # 获取当前日期
            current_date = datetime.now()

            # 将当前日期格式化为与 current_month_text 相同的格式
            formatted_current_date = current_date.strftime("%B %Y")

            if formatted_current_date != current_month_text:
                print(
                    f"\033[91mCurrent Month and Year are not Correct. Expected:"
                    f" {formatted_current_date}, Actual: {current_month_text}")

            # 使用空格分割文本，得到一个列表
            parts = current_month_text.split()
            # 提取月份和年份
            current_month = parts[0]
            current_year = int(parts[1])

            # Get target date components
            target_day = expected_date.day
            target_month = expected_date.month
            target_year = expected_date.year

            # Calculate the number of months to navigate (positive or negative)
            months_to_navigate = (target_year - current_year) * 12 + (target_month - month_number[current_month])

            # Navigate to the target month and year
            if months_to_navigate > 0:
                for _ in range(months_to_navigate):
                    product_page.click_calendar_next_button()
            else:
                for _ in range(-months_to_navigate):
                    product_page.click_calendar_prev_button()

            # Select the target day
            day_element = self.driver.find_element(By.XPATH, f"//td[@class='day' and text()='{target_day}']")
            day_element.click()
            time.sleep(1)

            product_page.click_add_to_cart_button()
            time.sleep(1)
            product_page.click_on_cart_button()
            time.sleep(1)
            product_page.click_on_Check_out_button()
            time.sleep(1)
            checkout_page = CheckOutPage(self.driver)
            checkout_page.remove_unavailable_products()
            time.sleep(1)
            checkout_page.click_on_payment_address_continue()
            time.sleep(1)
            checkout_page.click_on_delivery_details_continue()
            time.sleep(1)
            checkout_page.click_on_delivery_method_continue()
            time.sleep(1)
            checkout_page.click_on_payment_terms_agree()
            time.sleep(1)
            checkout_page.click_on_payment_method_button()
            time.sleep(2)
            actual_delivery_date = product_page.retrieve_delivery_date_text()
            actual_delivery_date_str = str(actual_delivery_date)

            expected_date_str = expected_date.strftime('%Y-%m-%d')
            assert expected_date_str in actual_delivery_date_str, f"Expected date: '{expected_date_str}' not found in actual delivery date: '{actual_delivery_date_str}'"

            checkout_page.click_on_confirm_order_button()
            time.sleep(1)
            actual_title = self.driver.title
            assert expected_text in actual_title, f"Expected text '{expected_text}' not found in page title"
            checkout_page.click_on_success_order_continue()

        except Exception as e:
            pytest.fail(f"An error occurred: {e}")

        time.sleep(1)
