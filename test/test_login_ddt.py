import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from utils.custom_logger import custom_logger

from pages.login_page import LoginPage
from utils.assertions import assert_text_contains, assert_element_visible
from utils.excel_utils import get_row_count, read_data
test_data = [
    ("tomsmith", "SuperSecretPassword!", "You logged into a secure area!"),
    ("tomsmith", "WrongPassword", "Your password is invalid!"),
    ("WrongUser", "SuperSecretPassword!", "Your username is invalid!"),
]

@pytest.mark.parametrize("username,password,expected", test_data)
def test_login_data_driven(username, password, expected):

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    login_page = LoginPage(driver)

    login_page.open()   # <-- FIXED

    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_login()

    flash = login_page.get_flash_message()
    
    assert_element_visible(flash)
    assert_text_contains(flash.text, expected)

    driver.quit()