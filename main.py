from playwright.sync_api import sync_playwright

def test_example():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://example.com")
        text = page.locator('h1').first.text_content()
        print(text) 
        browser.close()

test_example()
