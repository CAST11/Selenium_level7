import pytest

@pytest.mark.parametrize("username,password,expected", test_data)
def test_login_data_driven(driver, username, password, expected):
    # driver comes from conftest.py fixture

    login_page = LoginPage(driver)

    login_page.open()   # this should call driver.get()

    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_login()

    flash = login_page.get_flash_message()

    assert_element_visible(flash)
    assert_text_contains(flash.text, expected)
