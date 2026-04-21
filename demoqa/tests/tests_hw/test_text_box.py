from pages.text_box import TextBox
import time

def test_homework_10(browser):
    text_box_page = TextBox(browser)

    text_box_page.visit()
    text_box_page.full_name.send_keys('pink')
    time.sleep(1)
    text_box_page.current_address.send_keys('red')
    time.sleep(1)
    text_box_page.btn_submit.scroll_to_element()
    time.sleep(1)
    text_box_page.btn_submit.click()
    time.sleep(1)
    assert text_box_page.check_full_name.get_text() == 'Name:pink'
    time.sleep(1)
    assert text_box_page.check_current_address.get_text() == 'Name:pink\nCurrent Address :red'