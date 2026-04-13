from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://www.naver.com/")
    page.click("input[name='query']")
    page.keyboard.type("오늘의 날씨")
    page.keyboard.press("Enter")

    page.wait_for_timeout(5000)

    browser.close()