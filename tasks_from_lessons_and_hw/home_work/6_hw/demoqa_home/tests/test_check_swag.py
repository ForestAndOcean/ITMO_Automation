from pages.swag_labs import SwagLabs

def test_swag_labs(browser):
    swag_labs_page = SwagLabs(browser)
    # 1.1. перейти на страницу https://www.saucedemo.com/
    swag_labs_page.visit()
    # 1.2.проверить наличие иконки
    swag_labs_page.exist_icon()

    # 2.1. перейти на страницу https://www.saucedemo.com/
    swag_labs_page.visit()
    # 2.2. проверить наличие поля имени
    swag_labs_page.exist_field_name()

    # 3.1. перейти на страницу https://www.saucedemo.com/
    swag_labs_page.visit()
    # 3.2. проверить наличие поля пароля
    swag_labs_page.exist_field_password()