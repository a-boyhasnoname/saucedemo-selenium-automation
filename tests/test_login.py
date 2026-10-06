import pytest

from pages.inventory_page import InventoryPage
from utils.config import LOCKED_OUT_USER, PASSWORD, STANDARD_USER
from utils.test_data import INVALID_LOGIN_CASES


@pytest.mark.auth
@pytest.mark.smoke
def test_valid_login(login_page):
    login_page.login(STANDARD_USER, PASSWORD)
    inventory = InventoryPage(login_page.driver)

    assert inventory.is_loaded()
    assert inventory.get_title() == "Products"


@pytest.mark.auth
@pytest.mark.negative
@pytest.mark.parametrize("username,password,error_fragment", INVALID_LOGIN_CASES)
def test_invalid_login_cases(login_page, username, password, error_fragment):
    login_page.login(username, password)

    assert login_page.is_error_visible()
    assert error_fragment in login_page.get_error_message()


@pytest.mark.auth
@pytest.mark.negative
def test_locked_out_user_cannot_login(login_page):
    login_page.login(LOCKED_OUT_USER, PASSWORD)

    assert "locked out" in login_page.get_error_message().lower()


@pytest.mark.auth
def test_password_field_is_masked(login_page):
    password_input = login_page.find(login_page.PASSWORD)

    assert password_input.get_attribute("type") == "password"
