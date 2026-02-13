# tests/conftest.py
import pytest
from playwright.sync_api import Browser, Page, sync_playwright
from typing import Generator

@pytest.fixture(scope="session")
def browser() -> Generator[Browser, None, None]:
    """Create a browser instance for the test session"""
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,
            args=['--no-sandbox', '--disable-dev-shm-usage',
                   '--start-maximized','--window-size=1920,1080']
        )
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def page(browser: Browser) -> Generator[Page, None, None]:
    """Create a new page for each test"""
    context = browser.new_context(
        viewport={'width': 1920, 'height': 1080}
    )
    page = context.new_page()
    page.set_default_timeout(30000)  # 30 seconds
    yield page
    context.close()

@pytest.fixture(scope="function")
def authenticated_page(page: Page) -> Generator[Page, None, None]:
    """Create a page with admin already logged in"""
    # Login logic here
    page.goto("https://backoffice.uat.teresaapp.com/auth/login")
    page.get_by_role("textbox", name="Email").fill("admin")
    page.get_by_role("textbox", name="Password").fill("admin123")
    page.get_by_role("button", name="Login").click()
    page.wait_for_url("**/dashboard/**")
    yield page
