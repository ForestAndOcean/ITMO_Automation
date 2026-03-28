from selenium.common.exceptions import NoSuchElementException
from pages.base_page import BasePage
from components.components import WebElement

class Demoqa(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/'
        super().__init__(driver, self.base_url)
        self.icon = WebElement(driver, '#root > header > a')
        self.btn_elements = WebElement(driver, "#root > div > div > div.home-body > div > a:nth-child(1)")
        self.text_footer = WebElement(driver, '#root > footer > span')

    def exist_icon(self):
        try:
            self.icon.find_element()
        except NoSuchElementException:
            return False
        return True

    # def click_on_the_icon(self):
    #     self.find_element(locator = '#root > header > a').click()
    #
    # def click_on_the_btn(self):
    #     self.find_element(locator = "#app > div > div > div.home-body > div > div:nth-child(1)").click()