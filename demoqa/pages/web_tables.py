from pages.base_page import BasePage
from components.components import WebElement

class WebTables(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/webtables'
        super().__init__(driver, self.base_url)

        self.no_data = WebElement(driver, 'div.rt-noData')
        self.btn_delete_row = WebElement(driver, "[onclick='Delete()']")
        self.btn_add = WebElement(driver, '#addNewRecordButton')
        self.dia_win = WebElement(driver, '#userForm')
        self.btn_submit = WebElement(driver, '#submit')
        self.first_name = WebElement(driver, '#firstName')
        self.last_name = WebElement(driver, '#lastName')
        self.email = WebElement(driver, '#userEmail')
        self.age = WebElement(driver, '#age')
        self.salary = WebElement(driver, '#salary')
        self.department = WebElement(driver, '#department')
        self.forth_row = WebElement(driver, '#root > div > div > div > div.col-12.mt-4.col-md-6.col-xl-7 > div.container-fluid > div.web-tables-wrapper > table > tbody > tr:nth-child(4)')
        self.btn_pencil = WebElement(driver, '#edit-record-4')
        self.window_four = WebElement(driver, 'body > div.fade.modal.show > div > div')
        self.first_name_field_row_four = WebElement(driver, '#root > div > div > div > div.col-12.mt-4.col-md-6.col-xl-7 > div.container-fluid > div.web-tables-wrapper > table > tbody > tr:nth-child(4) > td:nth-child(1)')
        self.btn_delete_row_four = WebElement(driver, '#delete-record-4')