from pytest_playwright.pytest_playwright import page

from factory.page_factory import PageFactory
from utils.role_helpers import click_role, fill_role


def test_login_and_dashboard(page):
    app = PageFactory(page)

    # Step 1 — Login
    app.login.goto_login_page()
    # app.login.login("admin", "password123")
    app.login.enter_username("michael@example.com")
    click_role(page, "button", "username")
    # Step 2 — Check results
    assert app.dashboard.true_is_true() == True
