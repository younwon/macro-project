import asyncio
from playwright.async_api import async_playwright

async def run_nol():
    async with async_playwright() as p:
        # 1. 브라우저 실행 및 세션 로드 (상태 저장 파일 이름은 nol_state.json으로 관리해봐)
        browser = await p.chromium.launch(headless=False)
        
        # 만약 파일이 없으면 에러가 날 수 있으니 try-except나 조건문을 나중에 추가하면 좋아
        try:
            context = await browser.new_context(storage_state="nol_state.json")
        except:
            context = await browser.new_context()

        page = await context.new_page()

        # 2. 놀티켓 접속
        await page.goto("https://nolticket.com/") # 실제 주소로 변경 필요

        # 3. [미션] 로그인 상태인지 확인하는 로직 작성
        # 팁: 상단에 '로그아웃' 버튼이 보이면 로그인 된 것, '로그인' 버튼이 보이면 안 된 것.
        login_button = page.locator("text='로그인'")
        
        if await login_button.is_visible():
            print("놀티켓 로그인 필요. 로그인을 완료해 주세요.")
            # 여기서 수동 로그인을 시키거나, 코드로 로그인을 시도해
            input("로그인 완료 후 엔터를 누르세요...")
            await context.storage_state(path="nol_state.json")
        else:
            print("놀티켓 로그인 상태 유지 중")

        # 4. 특정 공연 상세 페이지로 이동해보기
        # 예: 공연 목록 중 첫 번째 공연 클릭
        # await page.click(".performance_item") 
        
        await page.wait_for_timeout(5000)
        await browser.close()

asyncio.run(run_nol())