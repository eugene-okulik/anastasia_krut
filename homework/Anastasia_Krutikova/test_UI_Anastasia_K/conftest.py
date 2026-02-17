import pytest
from playwright.sync_api import BrowserContext
from playwright.sync_api import Page
from pages.main_page import MainPage
from pages.desks_page import DesksPage
from pages.product_card_page import ProductCardPage
from pages.cart_page import CartPage


@pytest.fixture()
def page(context: BrowserContext):
    page = context.new_page()
    page.set_viewport_size({'width': 1920, 'height': 1080})
    return page


@pytest.fixture()
def main_page(page: Page):
    return MainPage(page)


@pytest.fixture()
def desks_page(page: Page):
    return DesksPage(page)


@pytest.fixture()
def product_card_page(page: Page):
    return ProductCardPage(page)


@pytest.fixture()
def cart_page(page: Page):
    return CartPage(page)
