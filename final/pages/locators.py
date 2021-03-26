from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, ".login_form")
    LOGININ_EMAIL_LINK = (By.CSS_SELECTOR, "#id_login_user-name")
    LOGININ_PASSWORD_LINK = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, ".login_form .btn-primary")


class RegisterPageLocators():
    REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, ".register_form .btn-primary")
    REGISTER_FORM = (By.CSS_SELECTOR, ".register_form")


class ProductPageLocators:
    PRODUCT_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".price_color")
    BASKET_PRICE = (By.CSS_SELECTOR, ".hidden-xs")
    PRODUCT_NAME = (By.CSS_SELECTOR, "h1")
    PRODUCT_SEARCH_TEXT = (By.CSS_SELECTOR, "#id_q")
    PRODUCT_SEARCH_BUTTON = (By.CSS_SELECTOR, "input.btn")


class AlertProductPageLocators:
    ALERT_BASKET_PRODUCT_NAME = (By.CSS_SELECTOR, ".in:nth-child(1)>.alertinner>strong")
    ALERT_BASKET_PRODUCT_PRICE = (By.CSS_SELECTOR, ".in:nth-child(3)>.alertinner")
    ALERT_SUCCESS = (By.CSS_SELECTOR, ".in:nth-child(1)")


class BasePageLocators:
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class SearchPageLocators:
    SEARCH_MATCH_TEXT = (By.CSS_SELECTOR, ".action h1")
    LIST_OF_SEARCHING_ELEMENTS = (By.CSS_SELECTOR, ".col-lg-3 h3")
    SEARCH_PAGE_SEARCH_TEXT = (By.CSS_SELECTOR, "#id_q")
    SEARCH_PAGE_SEARCH_BUTTON = (By.CSS_SELECTOR, "input.btn")
    SEARCH_PAGE_SEARCH_RESULT_NUMBER = (By.CSS_SELECTOR, ".form-horizontal")


class CataloguePageLocators:
    CATALOGUE_LIST_OF_ELEMENTS = (By.CSS_SELECTOR, ".col-lg-3 h3")
    CATALOGUE_SEARCH_BUTTON = (By.CSS_SELECTOR, "input.btn")
    CATALOGUE_NUMBER_OF_PRODUCTS = (By.CSS_SELECTOR, ".form-horizontal")
    CATALOGUE_SEARCH_TEXT = (By.CSS_SELECTOR, "#id_q")
