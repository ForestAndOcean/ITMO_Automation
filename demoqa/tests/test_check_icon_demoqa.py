# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# def test_check_icon():
#     driver = webdriver.Chrome()
#     driver.get("https://demoqa.com/")
#
#     icon = driver.find_element(By.CSS_SELECTOR, '#root > header > a')
#
#     if icon is None:
#         print('Элемент не найден')
#     else:
#         print('Элемент найден')

# аналогичная запись, но с использованием фикстуры (файл conftest.py)

# from selenium.webdriver.common.by import By
from pages.demoqa import Demoqa
import time

def test_check_icon(browser):
    # 1 browser.get("https://demoqa.com/")
    # 2
    # 3 icon = browser.find_element(By.CSS_SELECTOR, '#root > header > a')
    # 4
    # 5 if icon is None:
    # 6    print('Элемент не найден')
    # 7 else:
    # 8    print('Элемент найден')

    # то, что ниже = тому, что с # 1 по # 8

    demo_qa_page = Demoqa(browser)
    demo_qa_page.visit()
    time.sleep(3)
    demo_qa_page.icon.click()
    time.sleep(3)
    assert demo_qa_page.equal_url()
    assert demo_qa_page.exist_icon()
