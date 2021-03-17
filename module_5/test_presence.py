from .pages.locators import AlertProductPageLocators
from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators

class TestPresence:
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        #link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        try:
            page = ProductPage(browser, link)
            page.Open()

            #page.is_not_element_present(*ProductPageLocators.PRODUCT_NAME, timeout=5)

            page.should_be_product_page()

            page.add_to_basket()

            assert page.is_not_element_present(*AlertProductPageLocators.ALERT_SUCCESS,
                                               timeout=4) == True, "Success alert is presence"

        finally:
            print("over")

    def test_guest_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        try:
            page = ProductPage(browser, link)
            page.Open()

            #page.is_not_element_present(*ProductPageLocators.PRODUCT_NAME, timeout=4)

            page.should_be_product_page()

            assert page.is_not_element_present(*AlertProductPageLocators.ALERT_SUCCESS,
                                               timeout=4) == True, "Success alert is presence"
        finally:
            print("over")

    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        try:
            page = ProductPage(browser, link)
            page.Open()

            #page.is_not_element_present(*ProductPageLocators.PRODUCT_NAME, timeout=4)

            page.should_be_product_page()

            page.add_to_basket()

            assert page.is_disappeared(*AlertProductPageLocators.ALERT_SUCCESS,
                                       timeout=4) == True, "Success alert is disappeared"

        finally:
            print("over")

