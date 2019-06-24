import asyncio
from pyppeteer import launch


async def main():
    browser = await launch({'headless': False})
    page = await browser.newPage()
    await page.goto('http://www.baidu.com')
    await page.type('#kw', 'puppeteer', {'delay': 50})  # 在搜索框里慢慢输入puppeteer
    await page.click('#su')  # 然后点击搜索
    await page.waitFor(1000)
    # 点击第一个搜索结果
    targetLink = await page.evaluate('''() => {
        return document.querySelector('.result a').href
    }''')
    print(targetLink)
    await page.goto(targetLink)
    await page.waitFor(5000)
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())