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
        self.should_be_product_url()
        self.should_be_basket_button()

    def should_be_product_url(self):
        print("init url")
        self.product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        self.product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        self.url_product_name= self.product_name.lower().replace(" ","-").replace("'", "")
        print(self.product_name)

        assert self.browser.current_url.find(
            self.url_product_name) > -1, 'current productpage url is not correct'

    def should_be_basket_button(self):
        try:
            self.browser.find_element(*ProductPageLocators.PRODUCT_BASKET_BUTTON)
        except NoSuchElementException:
            return False
        return True

    def add_to_basket(self):
        btn_b = self.browser.find_element(*ProductPageLocators.PRODUCT_BASKET_BUTTON)

        btn_b.click()

        print("product was added to the basket")

    def read_price_in_basket(self):
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text

        pos1 = basket_price.find("£")
        pos2 = basket_price.find("\n")
        print("basket " + basket_price[pos1:pos2])
        print("product " + self.product_price)

        assert self.product_price == basket_price[
                                     pos1:pos2], f'your basket is {basket_price} and your product is {self.product_price}'

        #time.sleep(360)

    def read_add_basket_alert(self):
        print("prod name test")
        #try:
        alert_prod_name = self.browser.find_element(*AlertProductPageLocators.ALERT_BASKET_PRODUCT_NAME)
        text_name=alert_prod_name.text
        #except NoSuchElementException:
            #return False
        assert alert_prod_name.text == self.product_name, f'your prod name is {text_name} and {self.product_name}'

    def read_basket_sum_alert(self):
        try:
            alert_prod_price = self.browser.find_element(*AlertProductPageLocators.ALERT_BASKET_PRODUCT_PRICE).text
            print("-----"+alert_prod_price)
            pos1 = alert_prod_price.find("£")
            pos2 = alert_prod_price.find("\n")
        except NoSuchElementException:
            return False
        assert alert_prod_price[pos1:pos2] == self.product_price, f'your prod name is {alert_prod_price[pos1:pos2]}'
