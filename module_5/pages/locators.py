
from selenium.webdriver.common.by import By

class MainPageLocators():
	LOGIN_LINK=(By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
	LOGIN_FORM=(By.CSS_SELECTOR,"#login-form")
	LOGININ_EMAIL_LINK=(By.CSS_SELECTOR,"#id_login_user-name" )
	LOGININ_PASSWORD_LINK=(By.CSS_SELECTOR,"#id_login-password" )
	LOGIN_BUTTON=(By.CSS_SELECTOR, ".login_form/.btn-primary")

class RegisterPageLocators():
	REGISTER_EMAIL=(By.CSS_SELECTOR,"#id_registration-email")
	REGISTER_PASSWORD=(By.CSS_SELECTOR,"#id_registration-password1")
	REGISTER_CONFIRM_PASSWORD=(By.CSS_SELECTOR,"id_registration-password2")
	REGISTER_BUTTON=(By.CSS_SELECTOR,".register_form/.button-primary")
	REGISTER_FORM=(By.CSS_SELECTOR,"#register-form")

class ProductPageLocators():
	PRODUCT_BASKET_BUTTON=(By.CSS_SELECTOR, ".btn-add-to-basket")
	PRODUCT_PRICE=(By.CSS_SELECTOR, ".price_color")
	BASKET_PRICE=(By.CSS_SELECTOR, ".hidden-xs")
	PRODUCT_NAME=(By.CSS_SELECTOR, "h1")