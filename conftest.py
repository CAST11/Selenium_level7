import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

@pytest.fixture()
def setup(request):
    # Headless setup
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)
    #driver.maximize_window()
    #driver.set_window_size(1920, 1080)
    #request.cls.driver = driver
    #yield
    yield driver
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