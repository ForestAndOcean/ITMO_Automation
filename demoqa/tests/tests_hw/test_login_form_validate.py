from pages.form_page import FormPage
import time

def test_check_placeholder(browser):
    page_check = FormPage(browser)

    page_check.visit()
    assert page_check.first_name.get_dom_attribute('placeholder') == 'First Name'
    assert page_check.last_name.get_dom_attribute('placeholder') == 'Last Name'
    assert page_check.user_email.get_dom_attribute('placeholder') == 'name@example.com'
    assert page_check.user_email.get_dom_attribute('pattern') == \
           r'^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$'
    page_check.btn_submit.scroll_to_element()
    time.sleep(2)
    page_check.btn_submit.click()
    time.sleep(2)
    assert page_check.use_form.get_dom_attribute('class') == 'was-validated'