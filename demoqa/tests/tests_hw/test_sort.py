from pages.web_tables import WebTables
import time

def test_sort(browser):
    page_webtables = WebTables(browser)
    page_webtables.visit()