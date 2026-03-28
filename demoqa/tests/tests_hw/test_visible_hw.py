from pages.accordion import Accordion
import time

def test_visible_accordion(browser):
    accordion = Accordion(browser)
    accordion.visit()
    assert accordion.first_element_on_page_accordion.visible()
    accordion.second_element_on_page_accordion.click()
    time.sleep(2)
    assert not accordion.first_element_on_page_accordion.visible()

def test_visible_accordion_default(browser):
    accordion = Accordion(browser)
    accordion.visit()
    assert not accordion.third_element_on_page_accordion.visible()
    assert not accordion.fourth_element_on_page_accordion.visible()
    assert not accordion.fifth_element_on_page_accordion.visible()