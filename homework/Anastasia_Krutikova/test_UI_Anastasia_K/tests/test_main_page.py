def test_field_search_enable(main_page):
    main_page.open_page()
    main_page.check_search_field_enable()

def test_horizontal_scroll_enable(main_page):
    main_page.open_page()
    main_page.check_horizontal_scroll_enable()

def test_footer_text(main_page):
    main_page.open_page()
    main_page.footer_text("Copyright © Company name")
