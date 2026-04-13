from playwright.sync_api import sync_playwright

# p로 지칭 /  with은 start(),stop() 즉 리소스를 열고 정리를 자동으로 해줌
with sync_playwright() as p: 
    # 브라우저를 화면에 띄워서 실행
    browser = p.chromium.launch(headless=False)
    # p: playwright객체.크롬 기반 브라우저 엔진.브라우저실행(True은 백그라운드/False는 화면보임)
    page = browser.new_page()
    #브라우저 안에 탭 하나 생성/page는 탭 객체
    
    # 주소로 이동
    page.goto("https://www.naver.com/")
    
    # 페이지 제목 출력
    print(f"접속 성공! 페이지 제목: {page.title()}")
    # f"" = 값을 계산해서 포함하는 문자열 {}안의 식의 결과를 문자열에 포함시킨다
    # f의미는 f-string(문자열 포멧/string format)
    
    # 5초 동안 기다림/바로 닫히는거 방지
    page.wait_for_timeout(5000)
    #브라우저 종료 모든 탭 닫기
    browser.close()