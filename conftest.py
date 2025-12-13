import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import os
import datetime

@pytest.fixture()
def driver():
    options = Options()
    options.binary_location = "/usr/bin/google-chrome"

    # REQUIRED FOR JENKINS
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")

    # 🔥 LET SELENIUM MANAGER HANDLE CHROMEDRIVER
    driver = webdriver.Chrome(options=options)

    yield driver
    driver.quit()

# ----------------- Capture Screenshots on Test Failure -----------------
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()

    if result.when == "call" and result.failed:
        driver = getattr(item.cls, "driver", None)

        if driver:
            os.makedirs("reports/html", exist_ok=True)

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            screenshot_path = f"reports/html/screenshot_{timestamp}.png"

            driver.save_screenshot(screenshot_path)

            # Attach to pytest-html
            try:
                from pytest_html import extras
                if hasattr(result, "extra"):
                    result.extra.append(extras.image(screenshot_path))
            except ImportError:
                pass