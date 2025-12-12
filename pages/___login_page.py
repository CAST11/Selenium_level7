from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.custom_logger import custom_logger

class LoginPage:
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    FLASH_MESSAGE = (By.ID, "flash")

    def __init__(self, driver):
        self.driver = driver
        self.log = custom_logger()

    def open(self):
        self.driver.get("https://the-internet.herokuapp.com/login")
        login = LoginPage(self.driver) 
        login.open()   # <--- THIS WAS MISSING

    def enter_username(self, username):
        self.driver.find_element(*self.USERNAME).send_keys(username)
        self.log.info(f"Entering username: {username}")

    def enter_password(self, password):
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        

    def click_login(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()
        self.log.info("Clicking Login button")

    def get_flash_message(self):
        self.log.info("Getting validation message")
        return self.driver.find_element(*self.FLASH_MESSAGE)
        

    def get_flash_message(self):
        wait = WebDriverWait(self.driver, 5)
        return wait.until(EC.visibility_of_element_located((By.ID, "flash")))
    
    def click_logout_if_present(self):
        try:
            self.driver.find_element(By.XPATH, "//a[contains(text(),'Logout')]").click()
        except:
            pass