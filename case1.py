import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


link="http://selenium1py.pythonanywhere.com/ru/catalogue/"

try:

    browser=webdriver.Chrome()
    browser.get(link)
    time.sleep(5)

    browser.WebDriverWait(browser, 5).until(EC.presence_of_element_located(By.CSS_SELECTOR, "q"), message="not_elem")
    number_of_prod = browser.find_element_by_css_selector("q")
    print(number_of_prod)
    print(number_of_prod.text)
    assert int(number_of_prod.text)>0, "prodacts are not found"

    img_click=browser.WebDriverWait(browser, 5).until(EC.presence_of_element_located(By.CLASS_NAME, "thumbnail"))
    img_src=img_click.get_attribute("src")

    product_name=browser.find_element_by_css_selector("h3")
    product_name_text=product_name.text

    product_price=browser.find_element_by_class_name("price_color")
    product_price_text=product_price.text

    img_click.click()

finally:
    time.sleep(5)
    browser.quit()
#

