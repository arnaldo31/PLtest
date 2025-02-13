import os
from playwright.sync_api import sync_playwright

def test_example():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://example.com")

        # Extract <h1> text
        text = page.locator('h1').first.text_content()
        print(text)

        # Save text to a file (overwriting existing text.txt)
        with open('text.txt', 'w') as writer:
            writer.write(text)

        browser.close()

test_example()

# Automate Git commit and push inside GitHub Actions
if os.getenv("GITHUB_ACTIONS"):
    os.system("git config --global user.name 'github-actions[bot]'")
    os.system("git config --global user.email 'github-actions[bot]@users.noreply.github.com'")
    os.system("git add text.txt")
    os.system("git commit -m 'Auto-update text.txt'")
    os.system("git push")
