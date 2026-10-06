from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CartPage(BasePage):
    TITLE = (By.CSS_SELECTOR, "[data-test='title']")
    CART_ITEMS = (By.CSS_SELECTOR, "[data-test='cart-list'] [data-test='inventory-item']")
    ITEM_NAMES = (By.CSS_SELECTOR, "[data-test='inventory-item-name']")
    ITEM_PRICES = (By.CSS_SELECTOR, "[data-test='inventory-item-price']")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    CONTINUE_SHOPPING = (By.ID, "continue-shopping")

    def is_loaded(self) -> bool:
        return "cart" in self.driver.current_url and self.text(self.TITLE) == "Your Cart"

    def get_item_names(self) -> list[str]:
        if not self.is_visible(self.ITEM_NAMES, timeout=1):
            return []
        return self.texts(self.ITEM_NAMES)

    def get_item_prices(self) -> list[float]:
        if not self.is_visible(self.ITEM_PRICES, timeout=1):
            return []
        return [float(x.replace("$", "")) for x in self.texts(self.ITEM_PRICES)]

    def remove_product(self, product_name: str) -> None:
        xpath = (
            "//div[@data-test='inventory-item']"
            f"[.//div[@data-test='inventory-item-name' and normalize-space()='{product_name}']]"
            "//button[starts-with(@data-test,'remove')]"
        )
        self.click((By.XPATH, xpath))

    def checkout(self) -> None:
        self.click(self.CHECKOUT_BUTTON)

    def continue_shopping(self) -> None:
        self.click(self.CONTINUE_SHOPPING)
