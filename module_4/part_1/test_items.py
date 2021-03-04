import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_button(browser):
	browser.get(link)
	WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "btn-add-to-basket")))
	text=browser.find_element_by_class_name("btn-add-to-basket").text	
	
	assert text=="Add to basket", f"the button has another text: {text}"