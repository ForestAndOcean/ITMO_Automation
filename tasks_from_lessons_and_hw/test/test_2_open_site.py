# вход в браузер
from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://demoqa.com/')

# # поиск элемента
# icon = driver.find_element(By.CSS_SELECTOR, 'header > a > img')
# if icon is None:
#     print('Элемент не найден')
# else:
#     print('Элемент найден')