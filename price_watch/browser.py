async def render(page, url):
    await page.goto(url, wait_until="networkidle")
    return await page.content()
# persist storage state to skip the re-login
# skip unchanged pages with an ETag check
# handle empty result pages without erroring
# cap parallel browser pages to avoid OOM
