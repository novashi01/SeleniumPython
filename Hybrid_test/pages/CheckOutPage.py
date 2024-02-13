import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Hybrid_test.pages.BasePage import BasePage
from Hybrid_test.pages.LoginPage import LoginPage
from Hybrid_test.pages.RegisterPage import RegisterPage


class CheckOutPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    not_available_xpath = "//span[@class='text-danger']"
    renew_check_out_xpath = "//a[@class='btn btn-primary']"

    payment_address_continue_xpath = "//input[@id='button-payment-address']"
    existing_address_xpath = "//input[@value='existing']"
    new_address_xpath = "//input[@value='new']"

    delivery_details_continue_xpath = "//input[@id='button-shipping-address']"
    delivery_existing_address_xpath = "//*[@id='collapse-shipping-address']/div/form/div[1]/label"
    new_delivery_address_xpath = "//*[@id='collapse-shipping-address']/div/form/div[3]/label"
    delivery_method_continue_xpath = "//input[@id='button-shipping-method']"
    terms_agree_xpath = "//input[@name='agree']"
    no_payment_warning_xpath = "//div[@class='alert alert-warning alert-dismissible']"

    add_comments_area_xpath = "//textarea[@name='comment']"
    payment_method_button_xpath = "//input[@id='button-payment-method']"
    payment_method_warning_xpath = "//div[@class='alert alert-danger alert-dismissible']"
    confirm_order_button_xpath = "//input[@id='button-confirm']"
    success_order_information_css = "div[id='content'] h1"
    success_order_information_text = "Your order has been placed!"
    success_order_continue_xpath = "//a[@class='btn btn-primary']"

    def display_not_available_product(self):
        not_available_elements = self.driver.find_elements(By.XPATH, self.not_available_xpath)
        return len(not_available_elements) > 0

    def click_on_payment_address_continue(self):
        self.element_click("payment_address_continue_xpath",self.payment_address_continue_xpath)

    def click_on_delivery_details_continue(self):
        self.element_click("delivery_details_continue_xpath",self.delivery_details_continue_xpath)

    def click_on_delivery_method_continue(self):
        self.element_click("delivery_method_continue_xpath",self.delivery_method_continue_xpath)

    def click_on_payment_terms_agree(self):
        self.element_click("terms_agree_xpath",self.terms_agree_xpath)

    def retrieve_payment_warning_message(self):
        return self.retrieve_element_text("no_payment_warning_xpath",self.no_payment_warning_xpath)

    def click_on_payment_method_button(self):
        self.element_click("payment_method_button_xpath",self.payment_method_button_xpath)

    def click_on_confirm_order_button(self):
        self.element_click("confirm_order_button_xpath",self.confirm_order_button_xpath)

    def retrieve_success_order_message(self):
        return self.retrieve_element_text("success_order_information_link_text",self.success_order_information_css)

    def click_on_success_order_continue(self):
        self.element_click("success_order_continue_xpath",self.success_order_continue_xpath)

    def remove_unavailable_products(self):
        if self.display_not_available_product():
            # Unavailable products are displayed, remove them
            product_elements = self.driver.find_elements(By.XPATH, self.not_available_xpath)
            for product_element in product_elements:
                delete_button = product_element.find_element(By.XPATH, "//tbody/tr[1]/td[4]/div[1]/span[1]/button[2]")
                delete_button.click()
                # 等待一段时间，确保产品被删除
                time.sleep(1)
                self.element_click("renew_check_out_xpath", self.renew_check_out_xpath)










