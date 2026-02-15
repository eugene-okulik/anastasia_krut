from playwright.sync_api import Page, expect, BrowserContext


def test_one(page: Page):
    page.goto('https://www.qa-practice.com/elements/alert/confirm')
    page.on('dialog', lambda alert: alert.accept())
    page.locator('//*[@href="#"]').click()

    result_text = page.locator('#result')
    expect(result_text).to_contain_text("Ok")


def test_two(page: Page, context: BrowserContext):
    page.goto('https://www.qa-practice.com/elements/new_tab/button')

    link = page.locator('.a-button')

    with context.expect_page() as new_page_event:
        link.click()

    new_page = new_page_event.value

    result = new_page.locator('#result')
    expect(result).to_have_text('I am a new page in a new tab')

    new_page.close()

    page.locator('.a-button').is_enabled()


def test_three(page: Page):
    page.goto('https://demoqa.com/')

    page.get_by_text('Elements').click()

    page.get_by_text('Dynamic Properties').click()

    color_change = page.locator('#colorChange')

    expect(color_change).to_have_css('color', 'rgb(220, 53, 69)', timeout=10000)
    color_change.click()
