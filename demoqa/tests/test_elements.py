from pages.elements_page import ElementsPage

def test_find_elements(browser):
    object = ElementsPage(browser)

    object.visit()
    assert object.btns_first_menu.check_count_elements(count=9)