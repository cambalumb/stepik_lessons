import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en-GB",
                     help="Choose language: ru or en-gb")
    parser.addoption('--link', action='store', default=None, help="input url")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    link = request.config.getoption("link")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language, 'intl.accept_link': link})
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()
