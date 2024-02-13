from selenium.webdriver.common.by import By

from Hybrid_test.pages.BasePage import BasePage


class SearchPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    valid_hp_product_link_text = "HP LP3065"
    no_product_message_xpath = '//*[@id="content"]/p[2]'

    def display_status_of_product(self):
        return self.check_display_status_of_element("valid_hp_product_link_text",self.valid_hp_product_link_text)

    def retrieve_no_product_message(self):
        return self.retrieve_element_text("no_product_message_xpath",self.no_product_message_xpath)

    def click_valid_product(self):
        self.element_click("valid_hp_product_link_text",self.valid_hp_product_link_text)
