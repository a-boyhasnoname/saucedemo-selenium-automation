# Automation Test Plan

## 1. Project

**Application:** SauceDemo  
**URL:** https://www.saucedemo.com/  
**Automation stack:** Python + Selenium WebDriver + Pytest  
**Framework pattern:** Page Object Model (POM)

## 2. Objective

Automate stable, repeatable customer-facing regression scenarios for the SauceDemo e-commerce workflow. The suite is intended to provide fast feedback for authentication, product discovery, cart management, checkout, validation, and navigation behavior.

## 3. In Scope

- Login and login validation
- Locked-user behavior
- Product inventory rendering
- Product sorting
- Product detail navigation
- Add/remove cart operations
- Multiple-item cart behavior
- Checkout form validation
- Checkout overview
- Price calculations
- Successful checkout completion
- Logout
- Cart/session state checks
- Reset App State behavior

## 4. Out of Scope

- Performance/load testing
- API contract testing
- Database validation
- Visual regression pixel comparison
- Accessibility auditing
- Penetration/security testing
- Testing SauceDemo infrastructure itself

## 5. Automation Approach

The framework follows Page Object Model principles:

- **Tests** contain business assertions and scenarios.
- **Page objects** contain locators and page-specific interactions.
- **BasePage** contains shared WebDriver utilities and waits.
- **Fixtures** manage browser lifecycle and authenticated preconditions.
- **Utilities** contain configuration and reusable test data.

Explicit waits are preferred over arbitrary `sleep()` calls.

## 6. Browser Strategy

Supported by the framework:

- Google Chrome
- Mozilla Firefox

Headless mode is the default for fast execution and CI. Headed mode is available for local debugging.

## 7. Entry Criteria

- Python 3.10+ installed
- Chrome or Firefox installed
- Dependencies installed from `requirements.txt`
- SauceDemo is reachable

## 8. Exit Criteria

- Smoke suite passes for release confidence
- Regression suite has no unexplained critical failures
- Failure screenshots and HTML report are retained for investigation

## 9. Reporting

The framework supports:

- Pytest terminal output
- `pytest-html` self-contained report
- Automatic screenshots for failed tests
- GitHub Actions artifacts

## 10. CI Strategy

GitHub Actions executes the suite on:

- pushes to `main`
- pull requests targeting `main`
- manual workflow dispatch

The CI job installs Chrome and Python dependencies, executes the suite headlessly, and uploads the report/screenshots even when a test fails.

## 11. Risks

- UI locator changes can break automation even when functionality remains valid.
- Public demo data/behavior can change outside the test project's control.
- Browser/driver compatibility can affect local execution.
- Network instability can create environmental failures.

## 12. Maintenance Strategy

- Keep selectors inside page objects.
- Prefer stable `data-test` attributes.
- Avoid duplicated browser actions across tests.
- Add new test data to utility modules rather than hard-coding large datasets into tests.
- Review failed CI runs before changing expected results.
