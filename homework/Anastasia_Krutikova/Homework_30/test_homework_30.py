from playwright.sync_api import Page, expect, Route
import json


def test_iPhone_17(page: Page):

    expected_title = 'яблокофон 17 про'

    def handle_route(route: Route):

        response = route.fetch()
        body = response.json()
        body['body']['digitalMat'][0]['productName'] = expected_title
        body = json.dumps(body)

        route.fulfill(
            response=response,
            body=body
        )

    page.route('**/digital-mat?**', handle_route)
    page.goto('https://www.apple.com/shop/buy-iphone')

    page.locator('.rf-hcard-copy').first.click()

    result_title = page.locator('//*[@aria-controls="panel-:r29:-0"]')
    expect(result_title).to_have_text(expected_title)
