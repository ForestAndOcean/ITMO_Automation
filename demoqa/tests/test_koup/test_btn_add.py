from pages.herokuapp import Koup
from pages.herokuapp_add_remove_elements import KoupAdd
import time

def test_btn_add(browser):
    koup_page = Koup(browser)
    koup_add = KoupAdd(browser)

    koup_page.visit()
    assert koup_page.btn_add_remove_elements.get_text() == 'Add/Remove Elements'
    time.sleep(1)
    koup_page.btn_add_remove_elements.click()
    time.sleep(1)
    assert koup_add.equal_url()

    assert koup_add.btn_add_element.get_text() == 'Add Element'

    assert koup_add.btn_add_element.get_dom_attribute('onclick') == 'addElement()'

    # нажать на кнопку add element 4 раза
    for i in range(4):
        koup_add.btn_add_element.click()

    assert koup_add.btns_delete.check_count_elements(4)

    # проверка всех элементов
    for element in koup_add.btns_delete.find_elements():
        assert element.text == 'Delete'

    # проверка только первого элемента
    assert koup_add.btns_delete.get_text() == 'Delete'

    # кликнуть на каждую кнопку delete
    while koup_add.btns_delete.exist():
        koup_add.btns_delete.click()

    assert not koup_add.btns_delete.exist()