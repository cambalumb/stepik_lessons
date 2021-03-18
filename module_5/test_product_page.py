import pytest
import math
from selenium.common.exceptions import NoAlertPresentException
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from .pages.locators import AlertProductPageLocators
from .pages.main_page import MainPage
from .pages.locators import RegisterPageLocators
import time


# link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"

class TestProductPage:
    @pytest.mark.parametrize('promo_offer',
                             ["offer0", "offer1", "offer2", "offer3", "offer4", "offer5", "offer6",
                              pytest.param("offer7", marks=pytest.mark.xfail),
                              "offer8",
                              "offer9"])
    def test_guest_can_add_product_to_basket(self, browser, promo_offer):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=" + promo_offer
        page = ProductPage(browser, link)
        page.Open()

        page.get_class_properties()

        page.should_be_product_page()

        page.add_to_basket()

        solve_quiz_and_get_code(self, browser)

        page.read_price_in_basket()

        page.read_add_basket_alert()

        page.read_basket_sum_alert()

        print("page is " + link)


def solve_quiz_and_get_code(self, browser):
    alert = browser.switch_to.alert
    x = alert.text.split(" ")[2]
    answer = str(math.log(abs((12 * math.sin(float(x))))))
    alert.send_keys(answer)
    alert.accept()
    try:
        alert = browser.switch_to.alert
        alert_text = alert.text
        print(f"Your code: {alert_text}")
        alert.accept()
    except NoAlertPresentException:
        print("No second alert presented")


def guest_can_go_to_login_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/'
    page = MainPage(browser, link)
    page.Open()

    page.go_to_login_page()

    login_page = LoginPage(browser, browser.current_url)

    login_page.should_be_login_page()


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def test_setup(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/'
        email = str(time.time()) + "@email.org"
        passw = 'sdt6789Gh9F654'

        guest_can_go_to_login_page(browser)

        browser.find_element(*RegisterPageLocators.REGISTER_EMAIL).send_keys(email)
        browser.find_element(*RegisterPageLocators.REGISTER_PASSWORD).send_keys(passw)
        browser.find_element(*RegisterPageLocators.REGISTER_CONFIRM_PASSWORD).send_keys(passw)

        browser.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()

    @pytest.mark.xfail
    def test_user_cant_see_success_message_after_adding_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"

        page = ProductPage(browser, link)
        page.Open()

        page.get_class_properties()

        page.should_be_product_page()

        page.add_to_basket()

        assert page.is_not_element_present(*AlertProductPageLocators.ALERT_SUCCESS,
                                           timeout=4) == True, "Success alert is not presence"

    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        page = ProductPage(browser, link)
        page.Open()

        page.get_class_properties()

        page.should_be_product_page()

        page.add_to_basket()

        # solve_quiz_and_get_code(self, browser)

        page.read_price_in_basket()

        page.read_add_basket_alert()

        page.read_basket_sum_alert()

        print("page is " + link)
