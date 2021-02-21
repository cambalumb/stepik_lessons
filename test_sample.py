import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


link="http://selenium1py.pythonanywhere.com/ru/catalogue/"
browser = webdriver.Chrome()

def load_full_catalogue():
    browser.get(link)
    time.sleep(5)

    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "form-horizontal")))
    number_of_prod = browser.find_element_by_class_name("form-horizontal")
    print(number_of_prod.text)
    assert int(number_of_prod.text[0:3])>0, "prodacts are not found"
    return

def get_all_attributes_for_product():
    product_link=browser.find_element_by_xpath("//div/section/div[1]/ol/li/article/div/a").get_attribute("href")

    img_click=WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "thumbnail")))
    img_src=img_click.get_attribute("src")

    product_name=browser.find_element_by_xpath("//div/section/div[1]/ol/li/article/h3")
    product_name_text=product_name.text

    product_price=browser.find_element_by_class_name("price_color")
    product_price_text=product_price.text

    img_click.click()

    time.sleep(5)
    return product_link, product_name_text, img_src, product_price_text

def test_load_product_page():
    new_window = browser.window_handles[0]
    browser.switch_to.window(new_window)

    real_prod_link=browser.current_url
    assert real_prod_link==product_link, "you open another window"
    return

def test_product_name_on_product_page():
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".carousel-inner>.active")))
    product_name_text1 = browser.find_element_by_css_selector(".product_main>h1").text
    assert product_name_text == product_name_text1, f"product {product_name_text} name1 is not true"
    return

def test_product_name_navigator_on_prod_page():
    product_name_navigator=browser.find_element_by_css_selector(".breadcrumb>:nth-child(5)").text
    assert product_name_text==product_name_navigator, f"product {product_name_text} name from navigator is not valid"

def test_prod_price_on_prod_page():
    price1=browser.find_element_by_class_name("price_color").text
    assert product_price_text == price1, f"product {product_name_text} price1 {price1} is not true"
    return

def test_prod_price_from_discribe():
    price_from_describe=browser.find_element_by_css_selector(".table-striped>tbody>tr:nth-child(3)>td").text
    assert product_price_text == price_from_describe, f"product{product_name_text}  price_from_describe {price_from_describe} is not valid"
    return

def test_img_src_on_prod_page():
    img_src_1 = browser.find_element_by_css_selector(".carousel-inner>.active>:nth-child(1)").get_attribute("src")
    print(img_src)
    print(img_src_1)
    #assert img_src == img_src_1, "the image source is not true"
    return

def test_number_of_prod():
    avilabylity=browser.find_element_by_css_selector(".availability").text
    assert int(avilabylity[21:22])>0, f"{avilabylity} -number {product_name_text} is not valid"
    return

try:
	if __name__ == "__main__":
		load_full_catalogue()
		print("load_full_catalogue is passed")
		product_link, product_name_text, img_src, product_price_text = get_all_attributes_for_product()
		print("get_all_attributes_for_product is passed")
		test_load_product_page()
		print("test_load_product_page is passed")
		test_product_name_on_product_page()
		print("test_product_name_on_product_page is passed")
		test_product_name_navigator_on_prod_page()
		print("test_product_name_navigator_on_prod_page is passed")
		test_prod_price_on_prod_page()
		print("test_prod_price_on_prod_page is passed")
		test_prod_price_from_discribe()
		print("test_prod_price_from_discribe is passed")
		test_number_of_prod()
		print("test_number_of_prod is passed")
		
finally:
    time.sleep(5)
    browser.quit()
#

