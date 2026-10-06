import pytest

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from utils.test_data import CHECKOUT_VALID_DATA

BACKPACK = "Sauce Labs Backpack"
BIKE_LIGHT = "Sauce Labs Bike Light"


def start_checkout(inventory_page, products=(BACKPACK,)) -> CheckoutPage:
    for product in products:
        inventory_page.add_product(product)
    inventory_page.open_cart()
    CartPage(inventory_page.driver).checkout()
    return CheckoutPage(inventory_page.driver)


@pytest.mark.checkout
@pytest.mark.negative
@pytest.mark.parametrize(
    "first,last,postal,error_fragment",
    [
        ("", "Tester", "44600", "First Name is required"),
        ("QA", "", "44600", "Last Name is required"),
        ("QA", "Tester", "", "Postal Code is required"),
    ],
)
def test_checkout_required_field_validation(inventory_page, first, last, postal, error_fragment):
    checkout = start_checkout(inventory_page)
    checkout.fill_customer_info(first, last, postal)
    checkout.continue_checkout()

    assert error_fragment in checkout.get_error()


@pytest.mark.checkout
@pytest.mark.smoke
def test_valid_checkout_reaches_overview(inventory_page):
    checkout = start_checkout(inventory_page, products=(BACKPACK, BIKE_LIGHT))
    checkout.fill_customer_info(**CHECKOUT_VALID_DATA)
    checkout.continue_checkout()

    assert checkout.is_summary_loaded()
    assert set(checkout.get_summary_item_names()) == {BACKPACK, BIKE_LIGHT}


@pytest.mark.checkout
def test_checkout_subtotal_matches_item_prices(inventory_page):
    checkout = start_checkout(inventory_page, products=(BACKPACK, BIKE_LIGHT))
    checkout.fill_customer_info(**CHECKOUT_VALID_DATA)
    checkout.continue_checkout()

    expected_subtotal = round(sum(checkout.get_summary_item_prices()), 2)
    assert checkout.get_subtotal() == expected_subtotal


@pytest.mark.checkout
def test_checkout_total_equals_subtotal_plus_tax(inventory_page):
    checkout = start_checkout(inventory_page, products=(BACKPACK,))
    checkout.fill_customer_info(**CHECKOUT_VALID_DATA)
    checkout.continue_checkout()

    expected_total = round(checkout.get_subtotal() + checkout.get_tax(), 2)
    assert checkout.get_total() == expected_total


@pytest.mark.checkout
@pytest.mark.smoke
def test_complete_purchase(inventory_page):
    checkout = start_checkout(inventory_page, products=(BACKPACK,))
    checkout.fill_customer_info(**CHECKOUT_VALID_DATA)
    checkout.continue_checkout()
    checkout.finish()

    assert checkout.completion_header() == "Thank you for your order!"
    assert "checkout-complete" in checkout.driver.current_url
