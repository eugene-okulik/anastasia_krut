def test_add_to_cart(product_card_page):
    product_card_page.open_page()
    product_card_page.check_click_add_to_cart()
    product_card_page.check_toast_after_adding('Item(s) added to your cart')

def test_link_terms(product_card_page):
    product_card_page.open_page()
    product_card_page.check_terms_in_link_href()

def test_increase_count_products(product_card_page):
    product_card_page.open_page()
    product_card_page.check_increase_count(2)
