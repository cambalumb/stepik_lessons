from .base_page import BasePage
from .main_page import MainPage
from .locators import LoginPageLocators
from .locators import RegisterPageLocators


class LoginPage(MainPage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.browser.current_url.find('login') > -1, 'current url is not correct'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM) == True, "login form locator is not found"
        # self.browser.find_element(By.CSS_SELECTOR,*LoginPageLocators.LOGIN_FORM)

    def should_be_register_form(self):
        assert self.is_element_present(*RegisterPageLocators.REGISTER_FORM) == True, "register form locator is not found"
