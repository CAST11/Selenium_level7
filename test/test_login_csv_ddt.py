import pytest
from pages.login_page import LoginPage
from utils.read_csv import get_csv_data

data = get_csv_data("testdata/login_data.csv")


class TestLoginCSVDDT:

    @pytest.mark.parametrize("row", data)
    def test_login_csv_ddt(self, driver, row):
        username = row[0]
        password = row[1]
        expected = row[2]

        driver.get("https://the-internet.herokuapp.com/login")

        login_page = LoginPage(driver)
        login_page.enter_username(username)
        login_page.enter_password(password)
        login_page.click_login()

        flash = login_page.get_flash_message()
        assert expected in flash.text
