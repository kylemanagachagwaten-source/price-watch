async def render(page, url):
    await page.goto(url, wait_until="networkidle")
    return await page.content()
