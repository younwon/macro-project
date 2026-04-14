from playwright.async_api import async_playwright
import asyncio


async def run_nol(): #함수?
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()

        await page.goto("https://nol.interpark.com/ticket") # 놀 티켓 접속
        await page.wait_for_load_state("load") #대기

        await page.goto("https://accounts.yanolja.com/?clientId=ticket-pc&postProc=FULLSCREEN&origin=https%3A%2F%2Fnol.interpark.com%2Fticket&service=interpark-ticket&redirect=https%3A%2F%2Faccounts.interpark.com%2Flogin%2Fsuccess%2Fnol%3FpostProc%3DFULLSCREEN%26origin%3Dhttps%253A%252F%252Fnol.interpark.com%252Fticket&nol_device_id=175784238503581380")
        #login_btn = page.locator("menu li:has-text('로그인')") #로그인버튼 저장
        #await login_btn.click()
        

        await page.wait_for_timeout(5000)
        await browser.close()

asyncio.run(run_nol())