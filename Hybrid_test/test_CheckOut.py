import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Hybrid_test.pages.AccountPage import AccountPage
from Hybrid_test.pages.CheckOutPage import CheckOutPage
from Hybrid_test.pages.HomePage import HomePage
from Hybrid_test.pages.LoginPage import LoginPage
from Hybrid_test.pages.SearchPage import SearchPage
from Hybrid_test.BaseTest import BaseTest
from Hybrid_test.pages.WishListPage import WishListPage

expected_text = "Your order has been placed!"


class TestCheckOut(BaseTest):

    def test_wish_check_out_success(self):
        try:
            home_page = HomePage(self.driver)
            home_page.common_login()
            account_page = AccountPage(self.driver)
            account_page.click_on_wishlist_button()
            time.sleep(1)
            wish_list_page = WishListPage(self.driver)
            wish_list_page.add_to_cart_5()
            time.sleep(1)
            wish_list_page.click_on_cart_button()
            time.sleep(1)
            wish_list_page.click_on_Check_out_button()
            time.sleep(1)
            checkout_page = CheckOutPage(self.driver)
            checkout_page.remove_unavailable_products()
            time.sleep(2)
            checkout_page.click_on_payment_address_continue()
            time.sleep(1)
            checkout_page.click_on_delivery_details_continue()
            time.sleep(1)
            checkout_page.click_on_delivery_method_continue()
            time.sleep(1)
            checkout_page.click_on_payment_terms_agree()
            time.sleep(1)
            checkout_page.click_on_payment_method_button()
            time.sleep(1)
            checkout_page.click_on_confirm_order_button()
            time.sleep(3)
            actual_title = self.driver.title
            assert expected_text in actual_title, f"Expected text '{expected_text}' not found in page title"
            checkout_page.click_on_success_order_continue()
        except Exception as e:
            pytest.fail(f"An error occurred: {e}")

    def test_wish_check_out_1(self):
        try:
            home_page = HomePage(self.driver)
            home_page.common_login()
            account_page = AccountPage(self.driver)
            account_page.click_on_wishlist_button()
            time.sleep(1)
            wish_list_page = WishListPage(self.driver)
            wish_list_page.add_to_cart_1()
            time.sleep(1)
            wish_list_page.click_on_cart_button()
            time.sleep(1)
            wish_list_page.click_on_Check_out_button()
            time.sleep(1)
            checkout_page = CheckOutPage(self.driver)
            checkout_page.remove_unavailable_products()
            time.sleep(2)
            checkout_page.click_on_payment_address_continue()
            time.sleep(1)
            checkout_page.click_on_delivery_details_continue()
            time.sleep(1)
            checkout_page.click_on_delivery_method_continue()
            time.sleep(1)
            checkout_page.click_on_payment_terms_agree()
            time.sleep(1)
            checkout_page.click_on_payment_method_button()
            time.sleep(1)
            checkout_page.click_on_confirm_order_button()
            time.sleep(3)
            actual_title = self.driver.title
            assert expected_text in actual_title, f"Expected text '{expected_text}' not found in page title"
            checkout_page.click_on_success_order_continue()
        except Exception as e:
            pytest.fail(f"An error occurred: {e}")

    def test_wish_check_out_2(self):
        try:
            home_page = HomePage(self.driver)
            home_page.common_login()
            account_page = AccountPage(self.driver)
            account_page.click_on_wishlist_button()
            time.sleep(1)
            wish_list_page = WishListPage(self.driver)
            wish_list_page.add_to_cart_2()
            time.sleep(1)
            wish_list_page.click_on_cart_button()
            time.sleep(1)
            wish_list_page.click_on_Check_out_button()
            time.sleep(1)
            checkout_page = CheckOutPage(self.driver)
            checkout_page.remove_unavailable_products()
            time.sleep(2)
            checkout_page.click_on_payment_address_continue()
            time.sleep(1)
            checkout_page.click_on_delivery_details_continue()
            time.sleep(1)
            checkout_page.click_on_delivery_method_continue()
            time.sleep(1)
            checkout_page.click_on_payment_terms_agree()
            time.sleep(1)
            checkout_page.click_on_payment_method_button()
            time.sleep(1)
            checkout_page.click_on_confirm_order_button()
            time.sleep(3)
            actual_title = self.driver.title
            assert expected_text in actual_title, f"Expected text '{expected_text}' not found in page title"
            checkout_page.click_on_success_order_continue()
        except Exception as e:
            pytest.fail(f"An error occurred: {e}")

    def test_wish_check_out_3(self):
        try:
            home_page = HomePage(self.driver)
            home_page.common_login()
            account_page = AccountPage(self.driver)
            account_page.click_on_wishlist_button()
            time.sleep(1)
            wish_list_page = WishListPage(self.driver)
            wish_list_page.add_to_cart_3()
            time.sleep(1)
            wish_list_page.click_on_cart_button()
            time.sleep(1)
            wish_list_page.click_on_Check_out_button()
            time.sleep(1)
            checkout_page = CheckOutPage(self.driver)
            checkout_page.remove_unavailable_products()
            time.sleep(2)
            checkout_page.click_on_payment_address_continue()
            time.sleep(1)
            checkout_page.click_on_delivery_details_continue()
            time.sleep(1)
            checkout_page.click_on_delivery_method_continue()
            time.sleep(1)
            checkout_page.click_on_payment_terms_agree()
            time.sleep(1)
            checkout_page.click_on_payment_method_button()
            time.sleep(1)
            checkout_page.click_on_confirm_order_button()
            time.sleep(3)
            actual_title = self.driver.title
            assert expected_text in actual_title, f"Expected text '{expected_text}' not found in page title"
            checkout_page.click_on_success_order_continue()
        except Exception as e:
            pytest.fail(f"An error occurred: {e}")

    def test_wish_check_out_4(self):
        try:
            home_page = HomePage(self.driver)
            home_page.common_login()
            account_page = AccountPage(self.driver)
            account_page.click_on_wishlist_button()
            time.sleep(1)
            wish_list_page = WishListPage(self.driver)
            wish_list_page.add_to_cart_4()
            time.sleep(1)
            wish_list_page.click_on_cart_button()
            time.sleep(1)
            wish_list_page.click_on_Check_out_button()
            time.sleep(1)
            checkout_page = CheckOutPage(self.driver)
            checkout_page.remove_unavailable_products()
            time.sleep(2)
            checkout_page.click_on_payment_address_continue()
            time.sleep(1)
            checkout_page.click_on_delivery_details_continue()
            time.sleep(1)
            checkout_page.click_on_delivery_method_continue()
            time.sleep(1)
            checkout_page.click_on_payment_terms_agree()
            time.sleep(1)
            checkout_page.click_on_payment_method_button()
            time.sleep(1)
            checkout_page.click_on_confirm_order_button()
            time.sleep(3)
            actual_title = self.driver.title
            assert expected_text in actual_title, f"Expected text '{expected_text}' not found in page title"
            checkout_page.click_on_success_order_continue()
        except Exception as e:
            pytest.fail(f"An error occurred: {e}")





