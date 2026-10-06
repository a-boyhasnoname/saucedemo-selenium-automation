from datetime import datetime
from pathlib import Path

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from utils.config import PAGE_LOAD_TIMEOUT, PASSWORD, STANDARD_USER


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        choices=["chrome", "firefox"],
        help="Browser to run tests with: chrome or firefox",
    )
    parser.addoption(
        "--headed",
        action="store_true",
        default=False,
        help="Run browser with a visible UI. Headless is the default.",
    )


@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")
    headed = request.config.getoption("--headed")

    if browser == "chrome":
        options = ChromeOptions()
        if not headed:
            options.add_argument("--headless=new")
        options.add_argument("--window-size=1440,1000")
        options.add_argument("--disable-notifications")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        browser_driver = webdriver.Chrome(options=options)
    else:
        options = FirefoxOptions()
        if not headed:
            options.add_argument("-headless")
        browser_driver = webdriver.Firefox(options=options)
        browser_driver.set_window_size(1440, 1000)

    browser_driver.set_page_load_timeout(PAGE_LOAD_TIMEOUT)
    yield browser_driver
    browser_driver.quit()


@pytest.fixture
def login_page(driver):
    return LoginPage(driver).load()


@pytest.fixture
def logged_in_driver(driver):
    login = LoginPage(driver).load()
    login.login(STANDARD_USER, PASSWORD)
    inventory = InventoryPage(driver)
    assert inventory.is_loaded(), "Precondition failed: standard user could not log in"
    return driver


@pytest.fixture
def inventory_page(logged_in_driver):
    return InventoryPage(logged_in_driver)


def pytest_runtest_makereport(item, call):
    """Capture a screenshot automatically when a test fails."""
    if call.when != "call" or call.excinfo is None:
        return

    driver = item.funcargs.get("driver") or item.funcargs.get("logged_in_driver")
    if driver is None:
        return

    screenshot_dir = Path("screenshots")
    screenshot_dir.mkdir(exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_name = item.nodeid.replace("/", "_").replace("::", "__").replace("[", "_").replace("]", "")
    driver.save_screenshot(str(screenshot_dir / f"{safe_name}_{timestamp}.png"))
