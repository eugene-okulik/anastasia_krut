from pages.base_page import BasePage
from pages.locators import main_locators as loc
from playwright.sync_api import expect


class MainPage(BasePage):
    page_url = '/'

    def check_search_field_enable(self):
        search_field = self.find(loc.search_field_loc).first
        expect(search_field).to_be_enabled()

    def check_horizontal_scroll_enable(self):
        horizontal_scroll = self.find(loc.horizontal_scroll_loc)
        expect(horizontal_scroll).to_be_enabled()

    def footer_text(self, expected_text):
        footer_text = self.find(loc.footer_text_loc)
        expect(footer_text).to_have_text(expected_text)
