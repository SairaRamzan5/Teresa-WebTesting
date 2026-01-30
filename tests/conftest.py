# tests/conftest.py
import pytest
from playwright.sync_api import Page

@pytest.fixture
def login_as_admin(page: Page):
    """Fixture to login as admin before test"""
    print("🔐 Setting up: Logging in as admin...")
    
    # Go to login page
    page.goto("https://backoffice.uat.teresaapp.com/auth/login")
    
    # Wait for login form
    page.wait_for_selector('//input[@type="text"]', timeout=10000)
    
    # Fill credentials
    page.fill('//input[@type="text"]', "admin")
    page.fill('//input[@type="password"]', "admin123")
    
    # Click login
    page.click('button:has-text("Login")')
    
    # Wait for dashboard
    page.wait_for_selector('text="Welcome to Dashboard!"', timeout=15000)
    
    print("✅ Login fixture setup complete")
    
    yield page  # Test runs here
    
    # Teardown (optional)
    print("🧹 Cleaning up after test...")