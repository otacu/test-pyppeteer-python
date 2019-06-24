import asyncio
from pyppeteer import launch
from configparser import ConfigParser


async def main():
    cp = ConfigParser()
    cp.read("../config/onion.cfg", encoding='UTF-8')
    section = cp.sections()[0]
    login_url = cp.get(section, "login_url")
    username = cp.get(section, "user_name")
    password = cp.get(section, "password")

    browser = await launch({'headless': False})
    page = await browser.newPage()
    await page.goto(login_url)
    await page.type('#userName', username, {'delay': 50})
    await page.type('#passWord', password, {'delay': 50})
    await page.click('#login-btn')
    await page.waitFor(5000)
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())