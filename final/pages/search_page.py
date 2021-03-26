from .base_page import BasePage
from .locators import SearchPageLocators


class SearchPage(BasePage):
    search_text = 0

    # check page properties / url, match alert, match text
    def should_be_search_page(self):
        self.should_be_search_url()
        self.should_be_match_alert()

    def should_be_search_url(self):
        assert self.browser.current_url.find(
            "search") > -1, f'current  url is not correct {self.browser.current_url},' \
                            f' search page name is include search word'

    def should_be_match_alert(self):
        assert self.is_element_present(*SearchPageLocators.SEARCH_MATCH_TEXT) == True, \
            "Match alert is not presence"

    def should_be_match_text(self):
        assert self.browser.find_element(*SearchPageLocators.SEARCH_MATCH_TEXT).text.find(self.search_text) > -1, \
            f"matching text is not true {self.search_text}"

    # set class property / text for searching
    def get_search_page_properties(self, text):
        self.search_text = text

    # searching text should be in the name of a product
    def check_search_result_presence(self):
        elements = self.browser.find_elements(*SearchPageLocators.LIST_OF_SEARCHING_ELEMENTS)
        for element in elements:
            assert element.text.find(self.search_text) > -1, f'searching text not match your asking: ' \
                                                             f'{self.search_text}!={element.text} '

    # prepare test data
    def set_part_search_text(self):
        if len(self.search_text.split()) < 4:
            self.search_text = self.search_text.split()[-1]
        else:
            self.search_text = self.search_text.split()[1]

    def set_wrong_text(self):
        self.search_text = "!@#$%^&*(){}?|\'"

    # let searching in the search page
    def new_searching(self):
        search_element = self.browser.find_element(*SearchPageLocators.SEARCH_PAGE_SEARCH_TEXT)
        search_element.clear()
        search_element.send_keys(self.search_text)
        self.browser.find_element(*SearchPageLocators.SEARCH_PAGE_SEARCH_BUTTON).click()

    # check a number of finding results
    def check_search_results_number(self):
        result_number = self.browser.find_element(*SearchPageLocators.SEARCH_PAGE_SEARCH_RESULT_NUMBER).text.split()[1]
        assert int(result_number) > 0, "searching is not success"
