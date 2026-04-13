from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # 브라우저를 화면에 띄워서 실행
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    
    # NOL티켓 주소로 이동
    page.goto("https://www.naver.com/")
    
    # 페이지 제목 출력
    print(f"접속 성공! 페이지 제목: {page.title()}")
    
    # 5초 뒤에 종료
    page.wait_for_timeout(5000)
    browser.close()