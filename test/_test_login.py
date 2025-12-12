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
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

driver.get("https://the-internet.herokuapp.com/login")

# Create page object
login = LoginPage(driver)

# Use page methods
login.enter_username("tomsmith")
login.enter_password("SuperSecretPassword!")
login.click_login()

# Validate login
message = wait.until(EC.presence_of_element_located((By.ID, "flash"))).text

print("\nResult:")
print(message)

def test_password_strength():
    
    password = "SuperSecretPassword!"
    is_valid, messages = is_strong_password(password)
    assert is_valid, f"Password is weak: {messages}"


driver.quit()