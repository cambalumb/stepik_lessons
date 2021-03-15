from .pages.product_page import ProductPage
from selenium.common.exceptions import NoAlertPresentException
import math
import pytest


# link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"

class TestProductPage:
    @pytest.mark.parametrize('promo_offer',
                             {"offer0", "offer1", "offer2", "offer3", "offer4", "offer5", "offer6",
                                 #pytest.param("offer7", marks=pytest.mark.xfail),
                                 "offer8",
                                 "offer9"})
    def test_guest_can_add_product_to_basket(self, browser, promo_offer):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=" + promo_offer
        try:
            page = ProductPage(browser, link)
            page.Open()

            page.should_be_product_page()

            page.add_to_basket()

            solve_quiz_and_get_code(self, browser)

            page.read_price_in_basket()

            page.read_add_basket_alert()

            page.read_basket_sum_alert()
        finally:
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
