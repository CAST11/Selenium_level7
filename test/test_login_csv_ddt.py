import pytest
from pages.login_page import LoginPage
from utils.read_csv import get_csv_data


@pytest.mark.usefixtures("setup")
class TestLoginCSVDDT:

    data = get_csv_data("testdata/login_data.csv")

    @pytest.mark.parametrize("row", data)
    def test_login_csv_ddt(self, row):
        username = row[0]
        password = row[1]
        expected = row[2]

        self.driver.get("https://the-internet.herokuapp.com/login")
        login_page = LoginPage(self.driver)

        login_page.enter_username(username)
        login_page.enter_password(password)
        login_page.click_login()

        flash = login_page.get_flash_message()

        assert flash.is_displayed()
        assert expected in flash.text
