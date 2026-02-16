def test_empty_cart(cart_page):
    cart_page.open_page()
    cart_page.check_cart_text('Your cart is empty!')

def test_cart_after_add_product(cart_page, product_card_page):
    product_card_page.open_page()
    product_card_page.check_click_add_to_cart()
    cart_page.check_cart_without_empty_text('Your cart is empty!')
    cart_page.check_cart_total_is_displayed()

