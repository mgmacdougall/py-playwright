#!/bin/bash

# Root folder
PROJECT_ROOT="."

echo "Creating Playwright Python POM scaffold..."

# Create directories
mkdir -p $PROJECT_ROOT/{pages,factory,tests}

# -------------------------
# Base Page
# -------------------------
cat << 'EOF' > $PROJECT_ROOT/pages/base_page.py
class BasePage:
    def __init__(self, page):
        self.page = page

    def visit(self, url):
        self.page.goto(url, wait_until="networkidle")

    def click(self, locator):
        self.page.locator(locator).click()

    def type(self, locator, text):
        self.page.locator(locator).fill(text)

    def wait_for(self, locator):
        self.page.locator(locator).wait_for(state="visible")
EOF

# -------------------------
# Login Page
# -------------------------
cat << 'EOF' > $PROJECT_ROOT/pages/login_page.py
from pages.base_page import BasePage

class LoginPage(BasePage):

    USERNAME = "#username"
    PASSWORD = "#password"
    LOGIN_BTN = "#login"

    def login(self, username, password):
        self.type(self.USERNAME, username)
        self.type(self.PASSWORD, password)
        self.click(self.LOGIN_BTN)
EOF

# -------------------------
# Dashboard Page
# -------------------------
cat << 'EOF' > $PROJECT_ROOT/pages/dashboard_page.py
from pages.base_page import BasePage

class DashboardPage(BasePage):

    HEADER = "h1.dashboard-title"

    def assert_loaded(self):
        self.wait_for(self.HEADER)
EOF

# -------------------------
# Page Factory
# -------------------------
cat << 'EOF' > $PROJECT_ROOT/factory/page_factory.py
class PageFactory:
    def __init__(self, page):
        self.page = page

    @property
    def login(self):
        from pages.login_page import LoginPage
        return LoginPage(self.page)

    @property
    def dashboard(self):
        from pages.dashboard_page import DashboardPage
        return DashboardPage(self.page)
EOF

# -------------------------
# End-to-End Test
# -------------------------
cat << 'EOF' > $PROJECT_ROOT/tests/test_login_dashboard.py
from factory.page_factory import PageFactory

def test_login_and_dashboard(page):
    app = PageFactory(page)

    # Step 1 — Login
    app.login.visit("https://example.com/login")
    app.login.login("admin", "password123")

    # Step 2 — Dashboard
    app.dashboard.assert_loaded()
EOF

# -------------------------
# conftest.py
# -------------------------
cat << 'EOF' > $PROJECT_ROOT/conftest.py
import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page
        context.close()
        browser.close()
EOF

echo "Scaffold created successfully in: $PROJECT_ROOT"