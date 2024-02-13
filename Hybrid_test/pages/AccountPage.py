from selenium.webdriver.common.by import By

from Hybrid_test.pages.BasePage import BasePage


class AccountPage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)

    edit_your_account_information_option_link_text = "Edit your account information"
    wish_list_xpath = "//*[@id='wishlist-total']"

    def display_status_of_edit_account_option(self):
        return self.check_display_status_of_element("edit_your_account_information_option_link_text",
                                                    self.edit_your_account_information_option_link_text)

    def retrieve_warning_message(self):
        warning_element = self.driver.find_element(By.XPATH, "//div[@class='alert alert-danger alert-dismissible']")
        return warning_element.text

    def click_on_wishlist_button(self):
        self.element_click("wish_list_xpath",self.wish_list_xpath)

