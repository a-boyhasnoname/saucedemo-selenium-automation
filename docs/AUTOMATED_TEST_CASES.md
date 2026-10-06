# Automated Test Case Matrix

The suite currently expands to **29 Pytest cases** because parameterized functions execute multiple data sets.

| ID | Area | Automated Scenario | Priority | Marker |
|---|---|---|---|---|
| ATC-001 | Login | Valid standard-user login | Critical | smoke, auth |
| ATC-002 | Login | Invalid username | High | negative, auth |
| ATC-003 | Login | Invalid password | High | negative, auth |
| ATC-004 | Login | Blank username | High | negative, auth |
| ATC-005 | Login | Blank password | High | negative, auth |
| ATC-006 | Login | Blank username and password | High | negative, auth |
| ATC-007 | Login | Locked-out user rejected | High | negative, auth |
| ATC-008 | Login | Password field is masked | Medium | auth |
| ATC-009 | Inventory | Product list contains products/prices | Critical | smoke, inventory |
| ATC-010 | Inventory | Sort Name A to Z | Medium | inventory |
| ATC-011 | Inventory | Sort Name Z to A | Medium | inventory |
| ATC-012 | Inventory | Sort Price low to high | High | inventory |
| ATC-013 | Inventory | Sort Price high to low | High | inventory |
| ATC-014 | Inventory | Open product detail page | High | inventory |
| ATC-015 | Cart | Add one item updates cart badge | Critical | smoke, cart |
| ATC-016 | Cart | Add multiple products | Critical | cart |
| ATC-017 | Cart | Remove item from inventory | High | cart |
| ATC-018 | Cart | Remove item from cart | High | cart |
| ATC-019 | Cart | Continue shopping preserves cart | High | cart |
| ATC-020 | Checkout | First name required | High | negative, checkout |
| ATC-021 | Checkout | Last name required | High | negative, checkout |
| ATC-022 | Checkout | Postal code required | High | negative, checkout |
| ATC-023 | Checkout | Valid data reaches overview | Critical | smoke, checkout |
| ATC-024 | Checkout | Summary items match selected products | Critical | checkout |
| ATC-025 | Checkout | Subtotal equals item-price sum | Critical | checkout |
| ATC-026 | Checkout | Total equals subtotal plus tax | Critical | checkout |
| ATC-027 | Checkout | Complete purchase successfully | Critical | smoke, checkout |
| ATC-028 | Navigation | Logout returns to login | Critical | regression |
| ATC-029 | Session | Cart survives normal navigation | High | regression |
| ATC-030 | Session | Reset App State clears cart | High | regression |

> Note: the table lists 30 logical scenarios. The current source suite executes 29 collected Pytest cases because the valid checkout overview test verifies both navigation and selected-item integrity in a single automated case.
