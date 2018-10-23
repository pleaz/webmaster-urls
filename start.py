import asyncio
from pyppeteer import launch


async def main():
    browser = await launch()

    page = await browser.newPage()
    await page.setViewport({'width': 1440, 'height': 900})

    await page.goto('https://accounts.google.com/signin/v2/identifier?flowName=GlifWebSignIn&flowEntry=ServiceLogin')
    await page.tap('[id="Email"]')
    await page.keyboard.type('')
    await page.click('[id="next"]')
    await page.waitForNavigation()

    await page.tap('[id="Passwd"]')
    await page.keyboard.type('')
    await page.tap('[id="signIn"]')
    # await page.waitForNavigation()
    # page.setDefaultNavigationTimeout(2000)

    await page.goto('https://search.google.com/search-console')
    # page.setDefaultNavigationTimeout(2000)
    await page.tap('[aria-label="Search property"]')
    # await page.waitForNavigation()
    sites = await page.querySelectorAllEval('[role="option"]', '(nodes => nodes.map(n => n.innerText))')
    print(sites)

    page.setDefaultNavigationTimeout(4000)
    await page.screenshot({'path': 'example.png'})

    try:
        raise TimeoutError('Navigation Timeout Exceeded: 30000 ms exceeded')
    except Exception as error:
        html = await page.content()
        f = open("test.html", "w")
        f.write(html)
        print(error)

    html = await page.content()
    f = open("test.html", "w")
    f.write(html)

    await browser.close()
    # time.sleep(1000)


asyncio.get_event_loop().run_until_complete(main())
