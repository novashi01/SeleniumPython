import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from Hybrid_test.pages.HomePage import HomePage
from Hybrid_test.pages.SearchPage import SearchPage
from Hybrid_test.BaseTest import BaseTest


expected_text = "1 item(s)"


class TestAddToCart(BaseTest):

    def test_add_to_cart_1(self):
        home_page = HomePage(self.driver)
        home_page.add_to_cart_1()
        time.sleep(2)
        assert expected_text in home_page.retrieve_cart_total_text(), f"Expected text '{expected_text}' not found."

    def test_add_to_cart_2(self):
        home_page = HomePage(self.driver)
        home_page.add_to_cart_2()
        time.sleep(2)
        assert expected_text in home_page.retrieve_cart_total_text(), f"Expected text '{expected_text}' not found."

    def test_add_to_cart_3(self):
        home_page = HomePage(self.driver)
        home_page.add_to_cart_3()
        time.sleep(2)
        assert expected_text in home_page.retrieve_cart_total_text(), f"Expected text '{expected_text}' not found."

    def test_add_to_cart_4(self):
        home_page = HomePage(self.driver)
        home_page.add_to_cart_4()
        time.sleep(2)
        assert expected_text in home_page.retrieve_cart_total_text(), f"Expected text '{expected_text}' not found."


