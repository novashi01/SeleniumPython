from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Hybrid_test.pages.BasePage import BasePage
from Hybrid_test.pages.LoginPage import LoginPage
from Hybrid_test.pages.RegisterPage import RegisterPage


class WishListPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    add_to_cart_1_xpath = "//*[@id='content']/div[1]/table/tbody/tr[1]/td[6]/button"
    add_to_cart_2_xpath = "//*[@id='content']/div[1]/table/tbody/tr[2]/td[6]/button"
    add_to_cart_3_xpath = "//*[@id='content']/div[1]/table/tbody/tr[3]/td[6]/button"
    add_to_cart_4_xpath = "//*[@id='content']/div[1]/table/tbody/tr[4]/td[6]/button"
    add_to_cart_5_xpath = "//*[@id='content']/div[1]/table/tbody/tr[5]/td[6]/button"
    cart_total_text_id = "cart-total"
    cart_button_xpath = "//*[@id='cart']/button"
    cart_first_remove_xpath = "//tbody/tr[1]/td[5]/button[1]"
    cart_check_out_xpath = "//strong[normalize-space()='Checkout']"

    def add_to_cart_1(self):
        self.element_click("add_to_cart_1_xpath",self.add_to_cart_1_xpath)
        return WishListPage(self.driver)

    def add_to_cart_2(self):
        self.element_click("add_to_cart_2_xpath",self.add_to_cart_2_xpath)
        return WishListPage(self.driver)

    def add_to_cart_3(self):
        self.element_click("add_to_cart_3_xpath",self.add_to_cart_3_xpath)
        return WishListPage(self.driver)

    def add_to_cart_4(self):
        self.element_click("add_to_cart_4_xpath",self.add_to_cart_4_xpath)
        return WishListPage(self.driver)

    def add_to_cart_5(self):
        self.element_click("add_to_cart_5_xpath",self.add_to_cart_5_xpath)
        return WishListPage(self.driver)

    def retrieve_cart_total_text(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, self.cart_total_text_id))
        )
        return element.text

    def click_on_cart_button(self):
        self.element_click("cart_button_xpath",self.cart_button_xpath)

    def click_on_cart_remove_button(self):
        self.element_click("cart_first_remove_xpath",self.cart_first_remove_xpath)

    def click_on_Check_out_button(self):
        self.element_click("cart_check_out_xpath",self.cart_check_out_xpath)

