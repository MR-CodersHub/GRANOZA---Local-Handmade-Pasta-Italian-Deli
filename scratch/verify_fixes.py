import asyncio
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 1280, "height": 900})
        
        # 1. Catering page - Light mode
        await page.goto("http://localhost:8080/catering.html")
        await page.wait_for_load_state("networkidle")
        
        guida_el = page.locator(".catering-instructions-section")
        if await guida_el.count() > 0:
            await guida_el.screenshot(path="scratch/catering_guida_light.png")
            print("Captured catering_guida_light.png")
            
        form_el = page.locator("#catering-form-section")
        if await form_el.count() > 0:
            await form_el.screenshot(path="scratch/catering_form_light.png")
            print("Captured catering_form_light.png")

        # Catering page - Dark mode
        await page.evaluate("document.documentElement.setAttribute('data-theme', 'dark')")
        await page.wait_for_timeout(300)
        
        if await guida_el.count() > 0:
            await guida_el.screenshot(path="scratch/catering_guida_dark.png")
            print("Captured catering_guida_dark.png")
            
        if await form_el.count() > 0:
            await form_el.screenshot(path="scratch/catering_form_dark.png")
            print("Captured catering_form_dark.png")

        # 2. Blog page - Light mode
        await page.goto("http://localhost:8080/blog.html")
        await page.wait_for_load_state("networkidle")
        blog_grid = page.locator(".blog-grid-section")
        if await blog_grid.count() > 0:
            await blog_grid.screenshot(path="scratch/blog_grid_light.png")
            print("Captured blog_grid_light.png")

        # Blog page - Dark mode
        await page.evaluate("document.documentElement.setAttribute('data-theme', 'dark')")
        await page.wait_for_timeout(300)
        if await blog_grid.count() > 0:
            await blog_grid.screenshot(path="scratch/blog_grid_dark.png")
            print("Captured blog_grid_dark.png")

        # 3. Contact page - Light mode
        await page.goto("http://localhost:8080/contact.html")
        await page.wait_for_load_state("networkidle")
        map_sec = page.locator("#map-section")
        if await map_sec.count() > 0:
            await map_sec.scroll_into_view_if_needed()
            await page.wait_for_timeout(1000)
            await map_sec.screenshot(path="scratch/contact_map_light.png")
            print("Captured contact_map_light.png")

        # Contact page - Dark mode
        await page.evaluate("document.documentElement.setAttribute('data-theme', 'dark')")
        await page.wait_for_timeout(300)
        if await map_sec.count() > 0:
            await map_sec.screenshot(path="scratch/contact_map_dark.png")
            print("Captured contact_map_dark.png")

        # Also mobile viewport check (375px)
        await page.set_viewport_size({"width": 375, "height": 812})
        await page.evaluate("document.documentElement.setAttribute('data-theme', 'light')")
        await page.goto("http://localhost:8080/contact.html")
        await page.wait_for_load_state("networkidle")
        if await map_sec.count() > 0:
            await map_sec.scroll_into_view_if_needed()
            await page.wait_for_timeout(500)
            await map_sec.screenshot(path="scratch/contact_map_mobile.png")
            print("Captured contact_map_mobile.png")

        await browser.close()

asyncio.run(run())
