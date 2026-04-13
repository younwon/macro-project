from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)  # 창 보이게
    page = browser.new_page()
    
    page.goto("https://www.google.com")
    
    input("엔터 누르면 종료")
    browser.close()