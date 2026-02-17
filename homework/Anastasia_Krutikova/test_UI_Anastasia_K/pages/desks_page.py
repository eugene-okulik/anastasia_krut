from pages.base_page import BasePage
from pages.locators import desks_locators as loc
from playwright.sync_api import expect


class DesksPage(BasePage):
    page_url = 'shop/category/desks-1'

    def check_breadcrumbs_text(self, text):
        breadcrumbs = self.find(loc.breadcrumbs_desk_loc)
        expect(breadcrumbs).to_contain_text(text)

    def check_cart_icon_enable(self):
        cart_icon = self.find(loc.cart_icon_loc).first
        expect(cart_icon).to_be_enabled()

    def check_count_of_elements_legs(self, expected_elements):
        elements = self.find(loc.elements_legs_loc)
        form_checks = elements.locator(loc.form_checks_loc)
        expect(form_checks).to_have_count(expected_elements)
