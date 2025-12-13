from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    URL = "https://the-internet.herokuapp.com/login"

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def enter_username(self, username):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.ID, "username"))
        ).send_keys(username)

    def enter_password(self, password):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.ID, "password"))
        ).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    def flash_message(self):
        return WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.ID, "flash"))
        )



