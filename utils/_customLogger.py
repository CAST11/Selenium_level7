import pytest
from selenium.webdriver.common.by import By

from utilities.ExcelUtils import get_row_count, read_data
from utilities.customLogger import log
from pages.LoginPage import LoginPage


@pytest.mark.usefixtures("setup")
class TestLoginDDT:
    logger = log()

    def test_login_data_driven(self):
        self.logger.info("**** Starting DDT Login Test ****")

        path = "testdata/login_data.xlsx"
        row_count = get_row_count(path, "Sheet1")

        for r in range(2, row_count + 1):
            username = read_data(path, "Sheet1", r, 1)
            password = read_data(path, "Sheet1", r, 2)
            expected_msg = read_data(path, "Sheet1", r, 3)

            self.logger.info(f"Test Data → USER: {username}, PASS: {password}, EXPECTED: {expected_msg}")

            lp = LoginPage(self.driver)
            lp.enter_username(username)
            lp.enter_password(password)
            lp.click_login()

            try:
                actual_msg = self.driver.find_element(By.ID, "flash").text.strip()
            except:
                actual_msg = "NO MESSAGE FOUND"

            self.logger.info(f"Actual Message Found → {actual_msg}")

            if expected_msg in actual_msg:
                self.logger.info("Status: PASS")
                assert True
            else:
                self.logger.error("Status: FAIL")
                assert False

            lp.click_logout_if_present()

        self.logger.info("**** Finished DDT Login Test ****")