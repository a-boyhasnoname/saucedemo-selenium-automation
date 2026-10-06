from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ProductPage(BasePage):
    NAME = (By.CSS_SELECTOR, "[data-test='inventory-item-name']")
    DESCRIPTION = (By.CSS_SELECTOR, "[data-test='inventory-item-desc']")
    PRICE = (By.CSS_SELECTOR, "[data-test='inventory-item-price']")
    ADD_TO_CART = (By.CSS_SELECTOR, "button[data-test^='add-to-cart']")
    REMOVE = (By.CSS_SELECTOR, "button[data-test^='remove']")
    BACK_TO_PRODUCTS = (By.ID, "back-to-products")

    def get_name(self) -> str:
        return self.text(self.NAME)

    def add_to_cart(self) -> None:
        self.click(self.ADD_TO_CART)

    def remove_from_cart(self) -> None:
        self.click(self.REMOVE)

    def back_to_products(self) -> None:
        self.click(self.BACK_TO_PRODUCTS)
