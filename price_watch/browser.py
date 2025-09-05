async def render(page, url):
    await page.goto(url, wait_until="networkidle")
    return await page.content()
# persist storage state to skip the re-login
# skip unchanged pages with an ETag check
# handle empty result pages without erroring
# cap parallel browser pages to avoid OOM
# Playwright fallback for JS-rendered listings
# Playwright fallback for JS-rendered listings
# Playwright fallback for JS-rendered listings
# block images and fonts to speed up render
# incremental crawl — only refetch changed pages
# skip unchanged pages with an ETag check
# wait for networkidle before reading the DOM
# cap parallel browser pages to avoid OOM
# reuse one browser context across pages
# block images and fonts to speed up render
# handle pagination that loops back to page 1
# Playwright fallback for JS-rendered listings
