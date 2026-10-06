"""Reusable test data for data-driven tests."""

INVALID_LOGIN_CASES = [
    ("invalid_user", "secret_sauce", "Username and password do not match"),
    ("standard_user", "wrong_password", "Username and password do not match"),
    ("", "secret_sauce", "Username is required"),
    ("standard_user", "", "Password is required"),
    ("", "", "Username is required"),
]

CHECKOUT_VALID_DATA = {
    "first_name": "QA",
    "last_name": "Tester",
    "postal_code": "44600",
}
