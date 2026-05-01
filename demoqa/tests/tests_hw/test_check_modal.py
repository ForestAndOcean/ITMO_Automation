from pages.modal_dialogs import ModalDialogs
import time

def test_check_modal(browser):
    modal = ModalDialogs(browser)

    modal.visit()
    modal.button_small_modal.click()
    time.sleep(1)
    assert modal.window_small_modal.exist()
    time.sleep(1)
    modal.button_close_small_modal.click()
    time.sleep(1)
    assert not modal.window_small_modal.exist()
    time.sleep(1)
    modal.button_large_modal.click()
    time.sleep(1)
    assert modal.window_large_modal.exist()
    time.sleep(1)
    modal.button_close_large_modal.click()
    time.sleep(1)
    assert not modal.window_large_modal.exist()