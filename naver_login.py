from playwright.sync_api import sync_playwright
import pyperclip

USER_ID = "test123"
USER_PW = "test321"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    #context = browser.new_context() 쿠기 저장, 로그인 상태 등을 저장하는 계정? 같은 것(처음할때)
    context = browser.new_context(storage_state="state.json")
    page = context.new_page()

    did_login = False #로그인 상태 검사

    page.goto("https://www.naver.com/")

    #page.wait_for_load_state("load") #페이지 로딩 대기
    page.wait_for_selector("input[name='query']") #검색창이 나타나면

    if page.locator("a[href*='nidlogin']").is_visible(): #로그인 버튼(버튼 안에 하이퍼링크중 일부)로 검사
        print("로그인 안됨")

        page.goto("https://nid.naver.com/nidlogin.login?mode=form&url=https://www.naver.com/")
        page.click("input[name='id']")
        page.keyboard.type(USER_ID, delay=100) #타이핑
        page.wait_for_timeout(500)

        #pyperclip.copy(USER_ID) 붙여넣기 방법
        #page.keyboard.press("Control+V")

        page.click("input[name='pw']")
        page.keyboard.type(USER_PW, delay=100)
        page.wait_for_timeout(1000)

        page.click("button[type='submit']")
        page.wait_for_timeout(3000)

        if "naver.com" in page.url: #if "검사 url" in page.url(in page.url이니까 검사 url이면)
        #if "nidlogin" not in page.url: #(이건 not in page.url이니까 검사 url이 아니면/없으면)
            print("자동 로그인 성공")
            did_login = True
        else:
            print("자동 로그인 실패 수동으로 로그인")
            input("로그인 완료 후 엔터 누르세요")
            did_login = True
            page.goto("https://www.naver.com/")
            page.wait_for_selector("input[name='query']")
        
    else:
        print("로그인 상태 유지됨")

    if did_login:
        context.storage_state(path="state.json") #현재 로그인 상태를 파일로 저장
        #저장되는 것(쿠키, 로그인 세션, localStorage 등)
        #그래서 state.json파일 생성됨
        print("로그인 상태 저장 완료")

    page.wait_for_timeout(5000)
    browser.close()