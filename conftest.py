import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture()
def setup(request):
    driver = webdriver.Chrome()
    #driver.maximize_window()
    driver.set_window_size(1920, 1080)
    request.cls.driver = driver
    yield
    driver.quit()

# ----------------- Capture Screenshots on Test Failure -----------------
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()

    if result.when == "call" and result.failed:
        driver = item.funcargs.get("setup") or item.funcargs.get("request").cls.driver
        if driver:
            driver.save_screenshot("reports/html/screenshot.png")
            # Attach screenshot to HTML
            if hasattr(result, 'extra'):
                from pytest_html import extras
                result.extra.append(extras.png("reports/html/screenshot.png"))