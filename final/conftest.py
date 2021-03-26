import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default=None,
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: ru or en-GB")


@pytest.fixture(scope="function")
def browser(request):
    config_param = {}
    config_param["browser_name"] = request.config.getoption("--browser_name")
    config_param["language"] = request.config.getoption("--language")
    browser_name=config_param["browser_name"]
    language = config_param["language"]
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox(options=options)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
