from .base_page import BasePage
from .locators import ProductPageLocators
from .locators import AlertProductPageLocators
from selenium.common.exceptions import NoSuchElementException
import time


class ProductPage(BasePage):
    product_price = 0
    url_product_name = 0
    product_name=0

    def should_be_product_page(self):
        self.get_class_properties()
        self.should_be_product_url()
        self.should_be_basket_button()

    def get_class_properties(self):
        self.product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        self.product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        self.url_product_name = self.product_name.lower().replace(" ", "-").replace("'", "")

    def should_be_product_url(self):
        assert self.browser.current_url.find(
            self.url_product_name) > -1, f'current productpage url is not correct {self.browser.current_url},' \
                                         f' product name is {self.product_name}'

    def should_be_basket_button(self):
        try:
            self.browser.find_element(*ProductPageLocators.PRODUCT_BASKET_BUTTON)
        except NoSuchElementException:
            return False
        return True

    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.PRODUCT_BASKET_BUTTON).click()

        print("product was added to the basket")

    def read_price_in_basket(self):
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text

        start_price_text = basket_price.find("£")
        stop_price_text = basket_price.find("\n")

        print("basket " + basket_price[start_price_text:stop_price_text])
        print("product " + self.product_price)

        assert self.product_price == basket_price[
                                     start_price_text:stop_price_text], \
            f'your basket is {basket_price} and your product is {self.product_price}'


    def read_add_basket_alert(self):
        alert_prod_name = self.browser.find_element(*AlertProductPageLocators.ALERT_BASKET_PRODUCT_NAME).text

        assert alert_prod_name == self.product_name, f'basket prod name is {alert_prod_name}' \
                                                     f' but choosing {self.product_name}'

    def read_basket_sum_alert(self):
        try:
            alert_prod_price = self.browser.find_element(*AlertProductPageLocators.ALERT_BASKET_PRODUCT_PRICE).text
        except NoSuchElementException:
            return False
        start_price_text = alert_prod_price.find("£")
        stop_price_text = alert_prod_price.find("\n")

        assert alert_prod_price[start_price_text:stop_price_text] == self.product_price, \
            f'your basket product price is {alert_prod_price[start_price_text:stop_price_text]} ' \
            f'but anonced is {self.product_price}'

