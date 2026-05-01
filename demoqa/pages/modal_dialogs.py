from pages.base_page import BasePage
from components.components import WebElement

class ModalDialogs(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/modal-dialogs'
        super().__init__(driver, self.base_url)

        self.btns_third_menu = WebElement(driver, 'div:nth-child(3)> div > ul > li')
        self.main_icon = WebElement(driver, '#root > header > a > img')
        self.button_small_modal = WebElement(driver, '#showSmallModal')
        self.button_large_modal = WebElement(driver, '#showLargeModal')
        self.window_small_modal = WebElement(driver, 'body > div.fade.modal.show > div > div')
        self.window_large_modal = WebElement(driver, 'body > div.fade.modal.show > div > div')
        self.button_close_small_modal = WebElement(driver, '#closeSmallModal')
        self.button_close_large_modal = WebElement(driver, '#closeLargeModal')