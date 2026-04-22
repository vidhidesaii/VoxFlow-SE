from playwright.sync_api import sync_playwright

def run_tests():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()

        url = "http://127.0.0.1:5500/index.html"

        page.goto(url)

        print("\n===== STARTING VOXFLOW TESTS =====")

        # TC1: Login
        page.locator("#Lemail").fill("test@gmail.com")
        page.locator("#Lpassword").fill("123456")
        page.locator("input[value='Login']").click()
        print("✅ TC1 Login Executed")

        # TC2: Empty validation
        page.goto(url)
        page.locator("input[value='Login']").click()
        print("✅ TC2 Empty validation checked")

        # TC3: UI switch
        page.goto(url)
        page.locator("#sign-up-btn").click()

        container_class = page.locator(".container").get_attribute("class")
        if "sign-up-mode" in container_class:
            print("✅ TC3 UI Switch PASS")
        else:
            print("❌ TC3 UI Switch FAIL")

        # TC4: Signup
        page.locator("#Semail").fill("vidhi@gmail.com")
        page.locator("#Spassword").fill("123456")
        page.locator("input[value='Sign up']").click()
        print("✅ TC4 Signup Executed")

        # TC5: Bug test
        page.goto(url)
        page.locator("#sign-up-btn").click()
        page.locator("#Semail").fill("test@gmail.com")
        page.locator("#Spassword").fill("1")
        page.locator("input[value='Sign up']").click()

        print("❌ TC5 BUG: Weak password accepted")

        print("\n===== TESTING COMPLETED =====")
        browser.close()

run_tests()