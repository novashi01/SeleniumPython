import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Hybrid_test.pages.AccountPage import AccountPage
from Hybrid_test.pages.HomePage import HomePage
from Hybrid_test.pages.LoginPage import LoginPage
from Hybrid_test.pages.SearchPage import SearchPage
from Hybrid_test.BaseTest import BaseTest
from Hybrid_test.pages.WishListPage import WishListPage

expected_text = "1 item(s)"


class TestWishAddCart(BaseTest):

    def test_wish_add_to_cart_1(self):
        home_page = HomePage(self.driver)
        home_page.common_login()

        account_page = AccountPage(self.driver)
        account_page.click_on_wishlist_button()
        time.sleep(1)
        wish_list_page = WishListPage(self.driver)
        wish_list_page.add_to_cart_1()
        time.sleep(2)
        assert expected_text in wish_list_page.retrieve_cart_total_text(), f"Expected text '{expected_text}' not found."
        wish_list_page.click_on_cart_button()
        time.sleep(1)
        wish_list_page.click_on_cart_remove_button()


    def test_wish_add_to_cart_2(self):
        home_page = HomePage(self.driver)
        home_page.common_login()

        account_page = AccountPage(self.driver)
        account_page.click_on_wishlist_button()
        time.sleep(1)
        wish_list_page = WishListPage(self.driver)
        wish_list_page.add_to_cart_2()
        time.sleep(2)
        assert expected_text in wish_list_page.retrieve_cart_total_text(), f"Expected text '{expected_text}' not found."
        wish_list_page.click_on_cart_button()
        time.sleep(1)
        wish_list_page.click_on_cart_remove_button()

    def test_wish_add_to_cart_3(self):
        home_page = HomePage(self.driver)
        home_page.common_login()

        account_page = AccountPage(self.driver)
        account_page.click_on_wishlist_button()
        time.sleep(1)
        wish_list_page = WishListPage(self.driver)
        wish_list_page.add_to_cart_3()
        time.sleep(2)
        assert expected_text in wish_list_page.retrieve_cart_total_text(), f"Expected text '{expected_text}' not found."
        wish_list_page.click_on_cart_button()
        time.sleep(1)
        wish_list_page.click_on_cart_remove_button()

    def test_wish_add_to_cart_4(self):
        home_page = HomePage(self.driver)
        home_page.common_login()

        account_page = AccountPage(self.driver)
        account_page.click_on_wishlist_button()
        time.sleep(1)
        wish_list_page = WishListPage(self.driver)
        wish_list_page.add_to_cart_4()
        time.sleep(2)
        assert expected_text in wish_list_page.retrieve_cart_total_text(), f"Expected text '{expected_text}' not found."
        wish_list_page.click_on_cart_button()
        time.sleep(1)
        wish_list_page.click_on_cart_remove_button()

