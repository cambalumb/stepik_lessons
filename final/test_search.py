from .pages.search_page import SearchPage
from .pages.catalogue_page import CataloguePage
import pytest


# testing of a searching function
class TestSearch:
    link = "http://selenium1py.pythonanywhere.com/catalogue"  # start link
    search_page = 0  # search_page object

    # test right searching from catalogue
    def test_right_search_from_catalogue_by_whole_name(self, browser):
        self.open_search_page(browser)
        self.search_page.should_be_match_text()

    def test_right_search_from_catalogue_by_part_name(self, browser):
        self.open_search_page(browser)
        self.search_page.set_part_search_text()
        self.check_search_page()

    # test bad searching with specific simbols. If test is failed  the site was corrupted
    @pytest.mark.xfail
    def test_not_presence_product(self, browser):
        self.open_search_page(browser)
        self.search_page.set_wrong_text()
        self.check_search_page()

    # common action for test search
    def open_search_page(self, browser):
        # start from catalogue
        page = CataloguePage(browser, self.link)
        page.Open()
        # test catalogue page properties
        page.should_be_catalogue_url()
        # prepare test data
        page.check_number_of_products()
        page.set_product_name()
        # first  main test action
        page.search_product()
        # create search page object
        self.search_page = SearchPage(browser, browser.current_url)
        # check result page properties
        self.search_page.should_be_search_page()
        self.search_page.should_be_match_alert()
        self.search_page.get_search_page_properties(page.product_name)

    # common checking for search page
    def check_search_page(self):
        # second main test action
        self.search_page.new_searching()
        # check result page properties
        self.search_page.should_be_search_page()
        self.search_page.should_be_match_alert()
        self.search_page.should_be_match_text()
        # check base results
        self.search_page.check_search_results_number()
        self.search_page.check_search_result_presence()
