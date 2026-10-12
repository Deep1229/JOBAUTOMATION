
from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://www.selenium.dev/selenium/web/web-form.html")

    # 1. Fill in the form
    page.locator("input[name='my-text']").fill("Deepthi")
    page.locator("input[name='my-password']").fill("Practice123")
    page.locator("textarea[name='my-textarea']").fill(
        "Applying for a software engineering role."
    )
    page.locator("select[name='my-select']").select_option(label="Two")
    page.locator("#my-check-2").check()

    # 2. Review the form in the browser
    approval = input(
        "Review the application in the browser. "
        "Type APPROVE to continue: "
    )

    # 3. Check the approval
    if approval == "APPROVE":
        print("Review approved. Ready for the next step.")
    else:
        print("Application cancelled.")

    # 4. Close the browser
    browser.close()