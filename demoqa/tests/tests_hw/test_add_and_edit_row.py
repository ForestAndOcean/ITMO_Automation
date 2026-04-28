from pages.web_tables import WebTables
import time

def test_add_and_edit_row(browser):
    wt = WebTables(browser)

    wt.visit()
    # на странице имеется кнопка Add
    assert  wt.btn_add.exist()
    # по клику на кнопку Add открывается диалоговое окно
    wt.btn_add.click()
    assert wt.dia_win.exist()
    # в диалоге нельзя сохранить пустую форму
    wt.btn_submit.click()
    assert wt.dia_win.exist()
    # если заполнить все поля и нажать на кнопку Submit, то диалог закрывается
    wt.first_name.send_keys('1')
    time.sleep(1)
    wt.last_name.send_keys('2')
    time.sleep(1)
    wt.email.send_keys('3@gmail.com')
    time.sleep(1)
    wt.age.send_keys('4')
    time.sleep(1)
    wt.salary.send_keys('5')
    time.sleep(1)
    wt.department.send_keys('6')
    time.sleep(1)
    wt.btn_submit.click()
    time.sleep(1)
    assert not wt.dia_win.exist()
    time.sleep(1)
    # в таблицу добавляется новая запись с введенными данными
    assert wt.forth_row.exist()
    time.sleep(1)
    # если кликнуть на карандаш на строке записи
    wt.btn_pencil.click_force()
    time.sleep(1)
    # открывается диалог с введенными данными
    assert wt.window_four.exist()
    # если изменить имя и сохранить то в таблице обновятся данные
    wt.first_name.send_keys('1')
    time.sleep(1)
    wt.btn_submit.click()
    time.sleep(1)
    assert wt.first_name_field_row_four.get_text() == '11'
    time.sleep(1)
    # если нажать на корзину в строке записи - запись удаляется
    wt.btn_delete_row_four.click_force()
    time.sleep(1)
    assert not wt.forth_row.exist()
    time.sleep(2)