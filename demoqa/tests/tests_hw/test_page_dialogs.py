from pages.modal_dialogs import ModalDialogs
from pages.elements_page import ElementsPage

def test_modal_elements(browser):
    modal_dialogs = ModalDialogs(browser)
    modal_dialogs.visit()
    assert modal_dialogs.btns_third_menu.check_count_elements(count=5)

def test_navigation_modal(browser):
    modal_dialogs_2 = ModalDialogs(browser)
    modal_dialogs_2.visit()
    modal_dialogs_2.refresh()
    modal_dialogs_2.main_icon.click()
    browser.back()
    browser.set_window_size(900, 400)
    browser.forward()
    assert browser.equal_url()
    assert browser.title == 'demosite'
    browser.set_window_size(1000, 1000)