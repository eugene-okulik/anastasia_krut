def test_breadcrumbs_text(desks_page):
    desks_page.open_page()
    desks_page.check_breadcrumbs_text('Desks')

def test_cart_icon_enable(desks_page):
    desks_page.open_page()
    desks_page.check_cart_icon_enable()

def test_count_of_elements_legs(desks_page):
    desks_page.open_page()
    desks_page.check_count_of_elements_legs(3)
