from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Hybrid_test.pages.BasePage import BasePage
from Hybrid_test.pages.LoginPage import LoginPage
from Hybrid_test.pages.RegisterPage import RegisterPage


class ProductPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    delivery_date_calendar_name = "option[225]"
    calendar_button_xpath = "//i[@class='fa fa-calendar']"
    calendar_located_class = "datepicker"
    current_month_year_class = "picker-switch"
    calendar_next_xpath = "/html/body/div[3]/div/div[1]/table/thead/tr[1]/th[3]"
    calendar_prev_xpath = "/html/body/div[3]/div/div[1]/table/thead/tr[1]/th[1]"
    add_to_cart_button_id = "button-cart"
    cart_total_text_id = "cart-total"
    cart_button_xpath = "//*[@id='cart']/button"
    cart_first_remove_xpath = "//tbody/tr[1]/td[5]/button[1]"
    cart_check_out_xpath = "//strong[normalize-space()='Checkout']"
    check_delivery_date_xpath = '//*[@id="collapse-checkout-confirm"]/div/div[1]/table/tbody/tr/td[1]/small'

    def retrieve_current_month_year(self):
        self.element_click("calendar_button_xpath",self.calendar_button_xpath)
        return self.retrieve_element_text("current_month_year_class",self.current_month_year_class)

    def click_calendar_next_button(self):
        self.element_click("calendar_next_xpath",self.calendar_next_xpath)

    def click_calendar_prev_button(self):
        self.element_click("calendar_prev_xpath", self.calendar_prev_xpath)

    def click_add_to_cart_button(self):
        self.element_click("add_to_cart_button_id", self.add_to_cart_button_id)

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

    def retrieve_delivery_date_text(self):
        return self.retrieve_element_text("check_delivery_date_xpath",self.check_delivery_date_xpath)






