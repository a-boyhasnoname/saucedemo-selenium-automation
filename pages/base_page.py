from pathlib import Path
from typing import Iterable

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from utils.config import DEFAULT_TIMEOUT


class BasePage:
    """Common browser actions shared by all page objects."""

    def __init__(self, driver: WebDriver, timeout: int = DEFAULT_TIMEOUT):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self, url: str) -> None:
        self.driver.get(url)

    def find(self, locator) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_all(self, locator) -> list[WebElement]:
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def click(self, locator) -> None:
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def type(self, locator, text: str, clear: bool = True) -> None:
        element = self.find(locator)
        if clear:
            element.clear()
        element.send_keys(text)

    def text(self, locator) -> str:
        return self.find(locator).text.strip()

    def texts(self, locator) -> list[str]:
        return [element.text.strip() for element in self.find_all(locator)]

    def is_visible(self, locator, timeout: int = 3) -> bool:
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def wait_for_url_contains(self, value: str) -> bool:
        return self.wait.until(EC.url_contains(value))

    def wait_until_invisible(self, locator) -> bool:
        return self.wait.until(EC.invisibility_of_element_located(locator))

    def screenshot(self, path: str | Path) -> None:
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        self.driver.save_screenshot(str(path))
