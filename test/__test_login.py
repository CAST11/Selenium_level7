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

from pages.login_page import LoginPage
from utils.password_validator import is_strong_password
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage


def test_login_success(driver):
    driver.get("https://the-internet.herokuapp.com/login")

    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    flash_message = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "flash")))

    assert "You logged into a secure area!" in flash_message.text

