import pytest

from pages.product_page import ProductPage


@pytest.mark.inventory
@pytest.mark.smoke
def test_inventory_has_products(inventory_page):
    names = inventory_page.get_product_names()
    prices = inventory_page.get_product_prices()

    assert len(names) > 0
    assert len(names) == len(prices)
    assert all(price > 0 for price in prices)


@pytest.mark.inventory
def test_sort_products_name_a_to_z(inventory_page):
    inventory_page.sort_by_visible_text("Name (A to Z)")
    names = inventory_page.get_product_names()

    assert names == sorted(names)


@pytest.mark.inventory
def test_sort_products_name_z_to_a(inventory_page):
    inventory_page.sort_by_visible_text("Name (Z to A)")
    names = inventory_page.get_product_names()

    assert names == sorted(names, reverse=True)


@pytest.mark.inventory
def test_sort_products_price_low_to_high(inventory_page):
    inventory_page.sort_by_visible_text("Price (low to high)")
    prices = inventory_page.get_product_prices()

    assert prices == sorted(prices)


@pytest.mark.inventory
def test_sort_products_price_high_to_low(inventory_page):
    inventory_page.sort_by_visible_text("Price (high to low)")
    prices = inventory_page.get_product_prices()

    assert prices == sorted(prices, reverse=True)


@pytest.mark.inventory
def test_open_product_details(inventory_page):
    expected_name = "Sauce Labs Backpack"
    inventory_page.open_product(expected_name)
    product = ProductPage(inventory_page.driver)

    assert product.get_name() == expected_name
    assert "inventory-item" in inventory_page.driver.current_url
