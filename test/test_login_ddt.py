import pytest

from pages.login_page import LoginPage

test_data = [
    ("tomsmith", "SuperSecretPassword!", "You logged into a secure area!"),
    ("WrongUser", "SuperSecretPassword!", "Your username is invalid!"),
    ("tomsmith", "WrongPass", "Your password is invalid!")
]

@pytest.mark.parametrize("username,password,expected", test_data)
def test_login_data_driven(driver, username, password, expected):
    driver.get("https://the-internet.herokuapp.com/login")
    login_page = LoginPage(driver)

    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_login()

    flash = login_page.get_flash_message()
    assert flash.is_displayed()
    assert expected in flash.text

