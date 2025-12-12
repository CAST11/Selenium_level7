"""
Docstring for lesson7_login_page
"""
from selenium.webdriver.common.by import By

class LoginPage:

    # Constructor: receives the driver
    def __init__(self, driver):
        self.driver = driver

    # Locators
    username_input = (By.ID, "username")
    password_input = (By.ID, "password")
    login_button   = (By.CSS_SELECTOR, "button[type='submit']")

    # Actions
    def enter_username(self, username):
        self.driver.find_element(*self.username_input).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()
