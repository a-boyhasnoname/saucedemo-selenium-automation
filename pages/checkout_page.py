from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CheckoutPage(BasePage):
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE = (By.ID, "continue")
    CANCEL = (By.ID, "cancel")
    ERROR = (By.CSS_SELECTOR, "[data-test='error']")

    SUMMARY_CONTAINER = (By.CSS_SELECTOR, "[data-test='checkout-summary-container']")
    ITEM_NAMES = (By.CSS_SELECTOR, "[data-test='inventory-item-name']")
    ITEM_PRICES = (By.CSS_SELECTOR, "[data-test='inventory-item-price']")
    SUBTOTAL = (By.CSS_SELECTOR, "[data-test='subtotal-label']")
    TAX = (By.CSS_SELECTOR, "[data-test='tax-label']")
    TOTAL = (By.CSS_SELECTOR, "[data-test='total-label']")
    FINISH = (By.ID, "finish")

    COMPLETE_HEADER = (By.CSS_SELECTOR, "[data-test='complete-header']")
    COMPLETE_TEXT = (By.CSS_SELECTOR, "[data-test='complete-text']")
    BACK_HOME = (By.ID, "back-to-products")

    def fill_customer_info(self, first_name: str, last_name: str, postal_code: str) -> None:
        self.type(self.FIRST_NAME, first_name)
        self.type(self.LAST_NAME, last_name)
        self.type(self.POSTAL_CODE, postal_code)

    def continue_checkout(self) -> None:
        self.click(self.CONTINUE)

    def get_error(self) -> str:
        return self.text(self.ERROR)

    def is_summary_loaded(self) -> bool:
        return self.is_visible(self.SUMMARY_CONTAINER) and "checkout-step-two" in self.driver.current_url

    def get_summary_item_names(self) -> list[str]:
        return self.texts(self.ITEM_NAMES)

    def get_summary_item_prices(self) -> list[float]:
        return [float(x.replace("$", "")) for x in self.texts(self.ITEM_PRICES)]

    @staticmethod
    def _money_from_label(label: str) -> float:
        return float(label.split("$")[-1])

    def get_subtotal(self) -> float:
        return self._money_from_label(self.text(self.SUBTOTAL))

    def get_tax(self) -> float:
        return self._money_from_label(self.text(self.TAX))

    def get_total(self) -> float:
        return self._money_from_label(self.text(self.TOTAL))

    def finish(self) -> None:
        self.click(self.FINISH)

    def completion_header(self) -> str:
        return self.text(self.COMPLETE_HEADER)
