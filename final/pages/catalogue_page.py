from .base_page import BasePage
from .locators import CataloguePageLocators
from .locators import AlertProductPageLocators
from selenium.common.exceptions import NoSuchElementException


class CataloguePage(BasePage):
    product_name = 0

    # check catalogue page properties
    def should_be_catalogue_url(self):
        assert self.browser.current_url.find(
            'catalogue') > -1, f'current productpage url {self.browser.current_url},' \
                               f' is not included "catalogue"'

    # check how many products was found
    def check_number_of_products(self):
        number_of_products = \
            self.browser.find_element(*CataloguePageLocators.CATALOGUE_NUMBER_OF_PRODUCTS).text.split()[0]
        assert int(number_of_products) > 0, "products are absent in the catalogue"

    # set class property/ Product's name should be 2 and more words for good testing
    def set_product_name(self):
        search_product_name_list = self.browser.find_elements(*CataloguePageLocators.CATALOGUE_LIST_OF_ELEMENTS)
        for search_product_name in search_product_name_list:
            if len(search_product_name.text.split()) > 1:
                self.product_name = search_product_name.text
                # print(self.product_name)

    # find products by text
    def search_product(self):
        self.browser.find_element(*CataloguePageLocators.CATALOGUE_SEARCH_TEXT).send_keys(self.product_name)
        self.browser.find_element(*CataloguePageLocators.CATALOGUE_SEARCH_BUTTON).click()
