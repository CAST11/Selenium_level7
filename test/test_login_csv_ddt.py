import pytest
from pages.login_page import LoginPage
from utilities.read_csv import get_csv_data

# ✅ MUST be defined BEFORE the class
data = get_csv_data("testdata/login_data.csv")


class TestLoginCSVDDT:

    @pytest.mark.parametrize("row", data)
    def test_login_csv(self, driver, row):
        login = LoginPage(driver)
        login.open()

        login.enter_username(row["username"])
        login.enter_password(row["password"])
        login.click_login()

        flash = login.get_flash_message()
        assert row["expected"] in flash.text
