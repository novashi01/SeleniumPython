import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Hybrid_test.pages.AccountPage import AccountPage
from Hybrid_test.pages.BasePage import BasePage
from Hybrid_test.pages.LoginPage import LoginPage
from Hybrid_test.pages.RegisterPage import RegisterPage


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    search_box_field_name = "search"
    search_button_xpath = "//*[@id='search']/span"
    my_account_drop_menu_xpath = "//span[normalize-space()='My Account']"
    login_option_link_text = "Login"
    register_option_link_text = "Register"
    register_logout_link_text = "Logout"
    add_to_cart_1_xpath = "//*[@id='content']/div[2]/div[1]/div/div[3]/button[1]"
    add_to_cart_2_xpath = "//*[@id='content']/div[2]/div[2]/div/div[3]/button[1]"
    add_to_cart_3_xpath = "//*[@id='content']/div[2]/div[3]/div/div[3]/button[1]"
    add_to_cart_4_xpath = "//*[@id='content']/div[2]/div[4]/div/div[3]/button[1]"
    cart_total_text_id = "cart-total"

    def enter_product_into_search_box_field(self, product_name):
        self.type_into_element(product_name, "search_box_field_name", self.search_box_field_name)

    def click_on_search_button(self):
        self.element_click("search_button_xpath", self.search_button_xpath)

    def click_on_my_account_drop_menu(self):
        self.element_click("my_account_drop_menu_xpath", self.my_account_drop_menu_xpath)

    def select_login_option(self):
        self.element_click("login_option_link_text",self.login_option_link_text)
        return LoginPage(self.driver)

    def select_logout_option(self):
        self.element_click("register_logout_link_text",self.register_logout_link_text)
        return HomePage(self.driver)

    def navigate_to_login_option(self):
        self.click_on_my_account_drop_menu()
        return self.select_login_option()

    def select_register_option(self):
        self.element_click("register_option_link_text",self.register_option_link_text)
        return RegisterPage(self.driver)

    def navigate_to_register_option(self):
        self.click_on_my_account_drop_menu()
        return self.select_register_option()

    def search_for_a_product(self,product_name):
        self.enter_product_into_search_box_field(product_name)
        return self.click_on_search_button()

    def add_to_cart_1(self):
        self.element_click("add_to_cart_1_xpath",self.add_to_cart_1_xpath)
        return HomePage(self.driver)

    def add_to_cart_2(self):
        self.element_click("add_to_cart_2_xpath",self.add_to_cart_2_xpath)
        return HomePage(self.driver)

    def add_to_cart_3(self):
        self.element_click("add_to_cart_3_xpath",self.add_to_cart_3_xpath)
        return HomePage(self.driver)

    def add_to_cart_4(self):
        self.element_click("add_to_cart_4_xpath",self.add_to_cart_4_xpath)
        return HomePage(self.driver)

    def retrieve_cart_total_text(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, self.cart_total_text_id))
        )
        return element.text

    def common_login(self):
        home_page = HomePage(self.driver)
        home_page.click_on_my_account_drop_menu()

        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, home_page.login_option_link_text)))

        home_page.select_login_option()
        login_page = LoginPage(self.driver)
        login_page.enter_email_address("test02@test.co")
        login_page.enter_password("12345678")
        login_page.click_on_login_button()
        return AccountPage(self.driver)





