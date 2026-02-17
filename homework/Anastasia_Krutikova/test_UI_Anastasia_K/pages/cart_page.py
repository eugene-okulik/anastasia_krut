from pages.base_page import BasePage
from pages.locators import cart_locators as loc
from playwright.sync_api import expect


class CartPage(BasePage):

    page_url = '/shop/cart'

    def check_cart_text(self, expected_text):
        expect(self.find(loc.empty_title_loc)).to_contain_text(expected_text)

    def check_cart_without_empty_text(self, expected_text):
        self.open_page()
        expect(self.find(loc.empty_title_loc)).not_to_contain_text(expected_text)

    def check_cart_total_is_displayed(self):
        expect(self.find(loc.cart_total_loc)).to_be_visible()
