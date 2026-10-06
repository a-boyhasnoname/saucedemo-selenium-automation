import pytest

from pages.login_page import LoginPage

BACKPACK = "Sauce Labs Backpack"


@pytest.mark.regression
def test_logout_returns_to_login_page(inventory_page):
    inventory_page.logout()
    login = LoginPage(inventory_page.driver)

    assert login.is_visible(login.LOGIN_BUTTON)
    assert inventory_page.driver.current_url.rstrip("/") == "https://www.saucedemo.com"


@pytest.mark.regression
def test_cart_state_survives_normal_navigation(inventory_page):
    inventory_page.add_product(BACKPACK)
    inventory_page.open_cart()
    inventory_page.driver.back()

    assert inventory_page.is_loaded()
    assert inventory_page.cart_count() == 1


@pytest.mark.regression
def test_reset_app_state_clears_cart_badge(inventory_page):
    inventory_page.add_product(BACKPACK)
    assert inventory_page.cart_count() == 1

    inventory_page.reset_app_state()
    inventory_page.driver.refresh()

    assert inventory_page.cart_count() == 0
