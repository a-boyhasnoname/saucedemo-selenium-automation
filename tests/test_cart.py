import pytest

from pages.cart_page import CartPage

BACKPACK = "Sauce Labs Backpack"
BIKE_LIGHT = "Sauce Labs Bike Light"


@pytest.mark.cart
@pytest.mark.smoke
def test_add_single_product_updates_cart_badge(inventory_page):
    inventory_page.add_product(BACKPACK)

    assert inventory_page.cart_count() == 1


@pytest.mark.cart
def test_add_multiple_products_to_cart(inventory_page):
    inventory_page.add_product(BACKPACK)
    inventory_page.add_product(BIKE_LIGHT)
    inventory_page.open_cart()
    cart = CartPage(inventory_page.driver)

    assert cart.is_loaded()
    assert set(cart.get_item_names()) == {BACKPACK, BIKE_LIGHT}


@pytest.mark.cart
def test_remove_product_from_inventory(inventory_page):
    inventory_page.add_product(BACKPACK)
    assert inventory_page.cart_count() == 1

    inventory_page.remove_product(BACKPACK)

    assert inventory_page.cart_count() == 0


@pytest.mark.cart
def test_remove_product_from_cart(inventory_page):
    inventory_page.add_product(BACKPACK)
    inventory_page.open_cart()
    cart = CartPage(inventory_page.driver)

    cart.remove_product(BACKPACK)

    assert BACKPACK not in cart.get_item_names()


@pytest.mark.cart
def test_continue_shopping_returns_to_inventory(inventory_page):
    inventory_page.add_product(BACKPACK)
    inventory_page.open_cart()
    cart = CartPage(inventory_page.driver)

    cart.continue_shopping()

    assert inventory_page.is_loaded()
    assert inventory_page.cart_count() == 1
