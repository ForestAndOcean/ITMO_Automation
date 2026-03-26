# 1. Создайте функцию которая
# a. переходит на страницу https://www.saucedemo.com/
# b. находит элементы:
# i. текстовое поле username
# ii. текстовое поле password
# iii. кнопку submit
# c. Создайте условие, если элементы найдены - вывести в консоль текст “Элементы найдены”

from selenium.webdriver.common.by import By
from selenium import webdriver

def find_username_password_submit():
    driver = webdriver.Chrome()
    driver.get('https://www.saucedemo.com/')

    # поиск элемента
    username = driver.find_element(By.CSS_SELECTOR, '#user-name')
    if username is None:
        print('Элемент username не найден')
    else:
        print('Элемент username найден')

    password = driver.find_element(By.CSS_SELECTOR, '#password')
    if password is None:
        print('Элемент password не найден')
    else:
        print('Элемент password найден')

    submit = driver.find_element(By.CSS_SELECTOR, '.login-box [type="submit"]')
    if submit is None:
        print('Элемент submit не найден')
    else:
        return 'Элемент submit найден'

print(find_username_password_submit())