from pages.text_box import TextBox
import time

def test_text_box_submit(browser):
    obj_text_box = TextBox(browser)

    obj_text_box.visit()

    assert obj_text_box.btn_submit.check_css('color', 'rgba(255, 255, 255, 1)')
    assert obj_text_box.btn_submit.check_css('backgroundColor', 'rgba(13, 110, 253, 1)')
    assert obj_text_box.btn_submit.check_css('borderColor', 'rgb(13, 110, 253)')
