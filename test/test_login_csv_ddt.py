import pytest
import os
from pages.login_page import LoginPage
from utils.csv_utils import load_csv_data

CSV_PATH = os.path.join(os.path.dirname(__file__), "..", "testdata", "login_data.csv")
data = load_csv_data(CSV_PATH)

@pytest.mark.usefixtures("setup")
class TestLoginCSVDDT:

    @pytest.mark.parametrize("row", data)
    def test_login_csv(self, row):
        # ⭐ IMPORTANT: OPEN THE LOGIN PAGE
        self.driver.get("https://the-internet.herokuapp.com/login")

        login = LoginPage(self.driver)

        username = row["username"]
        password = row["password"]
        expected_text = row["expected"]

        login.enter_username(username)
        login.enter_password(password)
        login.click_login()

        assert expected_text in login.get_message()