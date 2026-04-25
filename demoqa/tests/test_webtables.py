import time
from pages.web_tables import WebTables

def test_tables(browser):
    wt = WebTables(browser)

    # проверка блока no rows found
    wt.visit()
    assert not wt.no_data.exist()

    # удаляем все записи
    while wt.btn_delete_row.exist():
        wt.btn_delete_row.click()

    time.sleep(3)
    assert wt.no_data.exist()