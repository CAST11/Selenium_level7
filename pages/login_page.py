from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.custom_logger import custom_logger

class LoginPage:
    log = custom_logger()

    def __init__(self, driver):
        self.driver = driver

    # Locators
    username_input = (By.ID, "username")
    password_input = (By.ID, "password")
    login_button = (By.CSS_SELECTOR, "button.radius")
    flash_message = (By.ID, "flash")

    def enter_username(self, username):
        self.log.info(f"Entering username: {username}")
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.username_input)
        ).send_keys(username)

    def enter_password(self, password):
        self.log.info(f"Entering password")
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.password_input)
        ).send_keys(password)

    def click_login(self):
        self.log.info("Clicking Login button")
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.login_button)
        ).click()

    def get_message(self):
        """Returns the success/error message text."""
        try:
            msg = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(self.flash_message)
            ).text
            return msg.strip()
        except:
            return ""
