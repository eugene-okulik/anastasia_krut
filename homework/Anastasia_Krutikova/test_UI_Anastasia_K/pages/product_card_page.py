from pages.base_page import BasePage
from pages.locators import product_card_locators as loc
from playwright.sync_api import expect

class ProductCardPage(BasePage):

    page_url = 'shop/furn-9999-office-design-software-7?category=9'

    def check_click_add_to_cart(self):
        self.find(loc.btn_add_to_cart_loc).click()
        expect(self.find(loc.cart_icon_counter_loc).first).to_have_text('1')

    def check_toast_after_adding(self, expected_text):
        expect(self.find(loc.toast_text_loc)).to_be_visible()
        toast_test = self.find(loc.toast_text_loc)
        expect(toast_test).to_have_text(expected_text)

    def check_terms_in_link_href(self):
        link = self.find(loc.link_loc)
        expect(link).to_have_attribute("href", "/terms")

    def check_increase_count(self, expected_count: int):
        expected = str(expected_count)
        increase_count = self.find(loc.btn_increase_loc)
        increase_count.click()

        expect(self.find(loc.quantity_form_loc)).to_have_value(expected, timeout=5000)
