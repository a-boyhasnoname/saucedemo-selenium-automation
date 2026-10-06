from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

from pages.base_page import BasePage


class InventoryPage(BasePage):
    TITLE = (By.CSS_SELECTOR, "[data-test='title']")
    INVENTORY_CONTAINER = (By.CSS_SELECTOR, "[data-test='inventory-container']")
    INVENTORY_ITEMS = (By.CSS_SELECTOR, "[data-test='inventory-item']")
    ITEM_NAMES = (By.CSS_SELECTOR, "[data-test='inventory-item-name']")
    ITEM_PRICES = (By.CSS_SELECTOR, "[data-test='inventory-item-price']")
    SORT_SELECT = (By.CSS_SELECTOR, "[data-test='product-sort-container']")
    CART_LINK = (By.CSS_SELECTOR, "[data-test='shopping-cart-link']")
    CART_BADGE = (By.CSS_SELECTOR, "[data-test='shopping-cart-badge']")
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")
    RESET_APP_LINK = (By.ID, "reset_sidebar_link")

    def is_loaded(self) -> bool:
        return self.is_visible(self.INVENTORY_CONTAINER) and "inventory" in self.driver.current_url

    def get_title(self) -> str:
        return self.text(self.TITLE)

    def get_product_names(self) -> list[str]:
        return self.texts(self.ITEM_NAMES)

    def get_product_prices(self) -> list[float]:
        prices = self.texts(self.ITEM_PRICES)
        return [float(price.replace("$", "")) for price in prices]

    def product_card(self, product_name: str):
        xpath = (
            "//div[@data-test='inventory-item']"
            f"[.//div[@data-test='inventory-item-name' and normalize-space()={self._xpath_literal(product_name)}]]"
        )
        return self.find((By.XPATH, xpath))

    @staticmethod
    def _xpath_literal(value: str) -> str:
        if "'" not in value:
            return f"'{value}'"
        if '"' not in value:
            return f'"{value}"'
        parts = value.split("'")
        return "concat(" + ", \"'\", ".join(f"'{part}'" for part in parts) + ")"

    def add_product(self, product_name: str) -> None:
        card = self.product_card(product_name)
        card.find_element(By.CSS_SELECTOR, "button[data-test^='add-to-cart']").click()

    def remove_product(self, product_name: str) -> None:
        card = self.product_card(product_name)
        card.find_element(By.CSS_SELECTOR, "button[data-test^='remove']").click()

    def open_product(self, product_name: str) -> None:
        card = self.product_card(product_name)
        card.find_element(By.CSS_SELECTOR, "[data-test='inventory-item-name']").click()

    def sort_by_visible_text(self, visible_text: str) -> None:
        Select(self.find(self.SORT_SELECT)).select_by_visible_text(visible_text)

    def cart_count(self) -> int:
        if not self.is_visible(self.CART_BADGE, timeout=1):
            return 0
        return int(self.text(self.CART_BADGE))

    def open_cart(self) -> None:
        self.click(self.CART_LINK)

    def open_menu(self) -> None:
        self.click(self.MENU_BUTTON)
        self.wait.until(EC.visibility_of_element_located(self.LOGOUT_LINK))

    def logout(self) -> None:
        self.open_menu()
        element = self.wait.until(EC.presence_of_element_located(self.LOGOUT_LINK))
        self.driver.execute_script("arguments[0].click();", element)

    def reset_app_state(self) -> None:
        self.open_menu()
        element = self.wait.until(EC.presence_of_element_located(self.RESET_APP_LINK))
        self.driver.execute_script("arguments[0].click();", element)
