from playwright.sync_api import Page, expect
import re
import time

def test_teresa_admin_can_login(page: Page):
    page.goto("https://backoffice.uat.teresaapp.com/auth/login")

    page.get_by_role("textbox", name="Email").fill("admin")
    page.get_by_role("textbox", name="Password").fill("admin123")

    page.get_by_role("button", name="Login").click()

    expect(page).to_have_url(re.compile(r".*/dashboard/?$"))

    page.get_by_text("Phone Whitelist").click()
    expect(page).to_have_url(re.compile(r".*/dashboard/phone-whitelist/?$"))

    page.locator("button:has(svg.lucide-funnel)").click()
    page.wait_for_timeout(500)
    page.get_by_role("option",name="Approved").click()
    time.sleep(5)     
    page.get_by_role("switch").first.click()
    time.sleep(5)  
    page.locator("button:has(svg.lucide-funnel)").click()
    page.wait_for_timeout(500)  
    page.get_by_role("option",name="Rejected").click()
    time.sleep(5)
    

