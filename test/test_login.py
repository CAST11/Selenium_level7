"""
Docstring for test_login
Go run the file: 
cd ~/Documents/Selenium/level7  - Go to the project folder

type: 
python3 -m test.test_login

Why to include __init__.py file on each folder?

Because Python only treats a folder as a module/package if it contains an __init__.py file.

Without it, Python does not search inside the folder for modules, and your imports fail.

"""
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from pages.login_page import LoginPage
from utils.password_validator import is_strong_password
from utils.assertions import (assert_text_contains, assert_element_visible, assert_url_contains)
from utils.custom_logger import custom_logger
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def test_login_success(driver):
    login = LoginPage(driver)
    login.open()

    login.enter_username("tomsmith")
    login.enter_password("SuperSecretPassword!")
    login.click_login()

    msg = login.get_flash_message()

    assert_element_visible(msg)
    assert_text_contains(msg.text, "You logged into a secure area!")
    assert_url_contains(driver, "secure")