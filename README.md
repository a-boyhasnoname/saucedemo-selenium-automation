# 🧪 SauceDemo Selenium Web Automation Testing Framework

[![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue.svg?style=flat-square&logo=python)](https://www.python.org/)
[![Selenium](https://img.shields.io/badge/Selenium-4.x-green.svg?style=flat-square&logo=selenium)](https://www.selenium.dev/)
[![Pytest](https://img.shields.io/badge/Pytest-8.x-yellow.svg?style=flat-square&logo=pytest)](https://docs.pytest.org/)
[![Framework](https://img.shields.io/badge/Pattern-Page%20Object%20Model-orange.svg?style=flat-square)](#page-object-model)
[![CI Workflow](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-blueviolet.svg?style=flat-square&logo=github-actions)](#ci-with-github-actions)

A professional, portfolio-grade end-to-end web automation testing framework for **[SauceDemo](https://www.saucedemo.com/)** designed with **Python**, **Selenium WebDriver**, **Pytest**, and **Page Object Model (POM)** architecture.

---

## 🎯 Framework Highlights

- **Maintainable Architecture**: Decoupled test scripts from page locators and interaction logic using the Page Object Model (POM).
- **Comprehensive Coverage**: 29 automated test cases (including data-driven scenarios) covering authentication, inventory management, sorting, shopping cart operations, checkout calculations, and navigation state.
- **Robust Exception & Timeout Handling**: Explicit Selenium Waits (`WebDriverWait`) for page state changes, sidebar animations, and elements.
- **Cross-Browser Support**: Configured for Headless & Headed execution on Chrome and Firefox via **Selenium Manager**.
- **Automated Failure Artifacts**: Built-in `conftest.py` hook automatically captures timestamped screenshots upon test failure into `screenshots/`.
- **Rich HTML Reporting**: Integration with `pytest-html` for generating self-contained HTML test execution reports.
- **Continuous Integration**: Pre-configured GitHub Actions CI workflow to run test suites headlessly on code push or pull request.

---

## 📊 Automated Test Coverage

| Functional Area | Automated Test Scenarios |
|---|---|
| **Authentication** | Valid login, invalid credentials (parametrized), required fields, locked-out user validation, password masking |
| **Inventory & Catalog** | Product list rendering, product names & pricing, 4-way sorting (A-Z, Z-A, Price Low-High, Price High-Low), product details view |
| **Shopping Cart** | Single & multi-item add/remove, badge counter updates, cart state persistence, back navigation |
| **Checkout Flow** | Information form validation (parametrized missing fields), order subtotal computation, tax rate calculation, total verification, order completion |
| **Navigation & Session** | Logout flow, sidebar reset app state, persistent cart state across page transitions |

---

## 🏗️ Project Architecture

```text
saucedemo-selenium-automation/
├── .github/
│   └── workflows/
│       └── selenium-tests.yml    # CI pipeline for automated testing
├── docs/
│   ├── AUTOMATION_TEST_PLAN.md   # Test plan & automation strategy
│   └── AUTOMATED_TEST_CASES.md   # Detailed test case specification matrix
├── pages/                        # Page Object Model (POM) layer
│   ├── base_page.py              # Base page wrapping Selenium WebDriver & Explicit Waits
│   ├── login_page.py             # Login page locators and interactions
│   ├── inventory_page.py         # Catalog, sorting, and sidebar operations
│   ├── product_page.py           # Product detail page interactions
│   ├── cart_page.py              # Cart management page
│   └── checkout_page.py          # Checkout steps (step 1, step 2 overview, step 3 complete)
├── tests/                        # Pytest Test Suites
│   ├── test_login.py             # Authentication tests
│   ├── test_inventory.py         # Product display and sorting tests
│   ├── test_cart.py              # Cart addition and removal tests
│   ├── test_checkout.py          # Checkout form & price calculation tests
│   └── test_navigation.py        # Logout, session state, and navigation tests
├── utils/                        # Utility & Configuration modules
│   ├── config.py                 # Environment constants, timeouts, and credentials
│   └── test_data.py              # Parametrized test data sources
├── reports/                      # Directory for generated HTML test reports
│   └── .gitkeep
├── screenshots/                  # Directory for auto-captured failure screenshots
│   └── .gitkeep
├── conftest.py                   # Pytest fixtures, driver management, and reporting hooks
├── pytest.ini                    # Pytest configuration & test markers
├── requirements.txt              # Project Python dependencies
├── run_tests.bat                 # Windows execution script
├── run_tests.sh                  # macOS/Linux execution script
├── .gitignore                    # Version control ignore patterns
└── README.md                     # Project documentation
```

---

## 📚 QA Documentation

- 📄 **[Automation Test Plan](docs/AUTOMATION_TEST_PLAN.md)**: Strategy, scope, environments, and entry/exit criteria.
- 📋 **[Automated Test Case Matrix](docs/AUTOMATED_TEST_CASES.md)**: Test IDs, descriptions, steps, and assertions.

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.10+** installed on your machine.
- **Google Chrome** or **Mozilla Firefox** browser installed.

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/saucedemo-selenium-automation.git
cd saucedemo-selenium-automation
```

### 2. Set Up Virtual Environment

**Windows (PowerShell / CMD):**
```powershell
python -m venv .venv
.venv\Scripts\activate
```

**macOS / Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

> **Note:** Modern Selenium uses **Selenium Manager** to manage browser drivers automatically, so manual downloading of `chromedriver` or `geckodriver` is not required.

---

## 🧪 Running the Tests

### Execute Full Test Suite (Headless Chrome Default)

```bash
pytest
```

### Run Tests in Headed Mode (Visible Browser UI)

```bash
pytest --headed
```

### Run Tests on Firefox

```bash
pytest --browser firefox
```

### Run Specific Test Suites by Marker

```bash
# Smoke tests only
pytest -m smoke

# Checkout & Regression tests
pytest -m checkout
pytest -m regression
```

### Run Specific Test File

```bash
pytest tests/test_login.py
```

### Run Using Batch / Shell Helper Scripts

- **Windows**: `.\run_tests.bat`
- **macOS / Linux**: `./run_tests.sh`

---

## 📈 Test Reports & Screenshots

### Generating HTML Execution Report

To run tests and generate a single, self-contained HTML report:

```bash
pytest --html=reports/report.html --self-contained-html
```

After execution, open `reports/report.html` in any web browser to review the visual test breakdown, execution durations, and logs.

### Failure Screenshots

If any test fails during execution, `conftest.py` automatically captures a screenshot of the browser viewport and saves it into `screenshots/` with a timestamp:

```text
screenshots/tests_test_navigation.py__test_logout_returns_to_login_page_20261006_120839.png
```

---

## 🧩 Page Object Model (POM) Design

The framework enforces strict separation between test logic and UI locators:

- **`BasePage`**: Contains reusable Selenium WebDriver wrappers (`find`, `click`, `type`, `is_visible`, `wait_until_invisible`, `screenshot`).
- **Page Classes (`pages/`)**: Encapsulate locators (using CSS / XPath) and domain actions (e.g., `inventory_page.add_product("Sauce Labs Backpack")`).
- **Test Modules (`tests/`)**: Focus purely on user flows, assertions, and test scenarios.

```python
# Sample readable test script structure
def test_add_single_product_updates_cart_badge(inventory_page):
    inventory_page.add_product("Sauce Labs Backpack")
    assert inventory_page.cart_count() == 1
```

---

## 🔄 CI/CD Integration with GitHub Actions

The repository includes a complete GitHub Actions workflow (`.github/workflows/selenium-tests.yml`) that:

1. Triggers on `push` and `pull_request` to the `main` branch.
2. Sets up Python and installs Google Chrome.
3. Installs dependencies from `requirements.txt`.
4. Executes the full Pytest test suite in headless mode.
5. Generates the HTML report and captures screenshots if tests fail.
6. Uploads `reports/` and `screenshots/` as pipeline artifacts.

---

## 🔑 Test Credentials

SauceDemo provides public demo testing credentials:

| Role | Username | Password | Notes |
|---|---|---|---|
| Standard User | `standard_user` | `secret_sauce` | Main user for all standard flows |
| Locked Out User | `locked_out_user` | `secret_sauce` | Validated in lock-out scenario |

---

## 📝 Portfolio Description Summary

> **Selenium WebDriver Web Automation Framework**: Scalable end-to-end automation framework built for SauceDemo using Python, Pytest, and Page Object Model (POM). Automates login, catalog sorting, cart operations, checkout tax calculations, and session navigation across 29 test scenarios with explicit waits, failure screenshots, HTML reports, and GitHub Actions CI.
