import pytest
from pages.login_page import LoginPage

class TestLoginCSVDDT:

    @pytest.mark.parametrize("row", data)
    def test_login_csv(self, driver, row):
        login = LoginPage(driver)
        login.open()

        login.enter_username(row["username"])
        login.enter_password(row["password"])
        login.click_login()

        assert row["expected"] in login.get_flash_message().text
