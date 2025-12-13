import pytest
import os
from pages.login_page import LoginPage
from utils.csv_utils import load_csv_data

CSV_PATH = os.path.join(os.path.dirname(__file__), "..", "testdata", "login_data.csv")
data = load_csv_data(CSV_PATH)

@pytest.mark.usefixtures("setup")
class TestLoginCSVDDT:

    @pytest.mark.parametrize("row", data)
    def test_login_csv(self, driver, row):
        login = LoginPage(driver)
        login.open()

        login.enter_username(row["username"])
        login.enter_password(row["password"])
        login.click_login()

        assert row["expected"] in login.get_flash_message().text