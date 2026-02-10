from playwright.sync_api import Page, expect
import re
import time

def test_teresa_admin_can_login(page: Page):
    page.goto("https://backoffice.uat.teresaapp.com/auth/login")


            
    print("Testing with correct credentials")

    page.get_by_role("textbox", name="Email").fill("admin")
    page.get_by_role("textbox", name="Password").fill("admin123")
    page.get_by_role("button", name="Login").click()
    page.wait_for_timeout(500)

  

    expect(page).to_have_url(re.compile(r".*/dashboard/?$"))

    page.get_by_text("Phone Whitelist").click()
    expect(page).to_have_url(re.compile(r".*/dashboard/phone-whitelist/?$"))

    page.locator("button:has(svg.lucide-funnel)").click()
    page.wait_for_timeout(500)

    page.get_by_role("option",name="Approved").click()
    time.sleep(5)     
    switches = page.get_by_role("switch")
    if switches.count()>0:
        switches.first.click()
        page.wait_for_timeout(500)
        print("Clicked on approved item")
    else:
        print("No approved item found : skpping switch")
        page.wait_for_timeout(500)   

    page.locator("button:has(svg.lucide-funnel)").click()
    page.wait_for_timeout(500)

    page.get_by_role("option",name="Rejected").click()
    page.wait_for_timeout(500)
    switches = page.get_by_role("switch")
    if switches.count()>0:
        switches.first.click()
        page.wait_for_timeout(500)
        print("Rejected option found")
    else:
        print("Rejected not found: skipping switch")
        page.wait_for_timeout(500)

    page.get_by_placeholder("Search").fill("LOrenzo")
    page.wait_for_timeout(500)
    page.get_by_placeholder("Search").fill("Lorenzo")
    page.wait_for_timeout(500)
    page.get_by_placeholder("Search").fill("---323sdsf")
    page.wait_for_timeout(500)
    page.get_by_text("Products").click()
    expect(page).to_have_url(re.compile(r".*/dashboard/products?$"))
    page.wait_for_timeout(300)
    page.locator('span[data-slot="badge"]:has-text("pending")').first.click()
    page.wait_for_timeout(500)
    # page.get_by_role("button", name="Approve").click()
    page.locator("button:has-text('Approve')").click()
    page.get_by_placeholder("Search").fill("Oliviaa")
    page.wait_for_timeout(500)
    page.get_by_placeholder("Search").fill("think out of the box")
    page.wait_for_timeout(500)

    time.sleep(10)
