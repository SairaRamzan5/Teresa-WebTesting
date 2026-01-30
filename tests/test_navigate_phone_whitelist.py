# tests/test_navigate_phone_whitelist.py
from playwright.sync_api import Page, expect
import pytest
import time

def test_navigate_to_phone_whitelist(page: Page):
    """Test ONLY navigation to Phone Whitelist page"""
    print("🧪 Test 2: Navigate to Phone Whitelist")
    
    # ====== FIRST: LOGIN ======
    print("\n🔐 Step 1: Logging in...")
    
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
    print("✅ Login successful!")
    
    # ====== SECOND: NAVIGATE TO PHONE WHITELIST ======
    print("\n📍 Step 2: Navigating to Phone Whitelist...")
    
    # Click Phone Whitelist in sidebar
    page.click('text="Phone Whitelist"')
    
    # Wait for Phone Whitelist page to load
    # ❌ WRONG: page.wait_for_load_state('text="Phone Number...") 
    # ✅ CORRECT: Wait for the ELEMENT
    page.wait_for_selector('text="Phone Number Whitelist Management"', timeout=10000)
    
    # Wait for page to fully load
    page.wait_for_load_state("networkidle")
    time.sleep(2)  # Extra wait for React
    
    # Verify we're on the right page
    expect(page.locator('text="Total Numbers"')).to_be_visible()
    expect(page.locator('text="Pending Approvals"')).to_be_visible()
    expect(page.locator('table')).to_be_visible()
    
    # Check URL
    current_url = page.evaluate("() => window.location.href")
    print(f"📌 Current URL: {current_url}")
    
    # Take screenshot
    page.screenshot(path="reports/test2_phone_whitelist_page.png")
    
    print("\n✅ Navigation test passed!")
    print("📸 Screenshot saved: reports/test2_phone_whitelist_page.png")