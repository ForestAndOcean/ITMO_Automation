from pages.base_page import BasePage
from components.components import WebElement

class Accordion(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://demoqa.com/accordian'
        super().__init__(driver, self.base_url)

        self.first_element_on_page_accordion = WebElement(driver, '#accordianContainer > div > div:nth-child(1) > div > div > p')
        self.second_element_on_page_accordion = WebElement(driver, '#accordianContainer > div > div:nth-child(1) > h2 > button')
        self.third_element_on_page_accordion = WebElement(driver,'#accordianContainer > div > div:nth-child(2) > div > div > p:nth-child(1)')
        self.fourth_element_on_page_accordion = WebElement(driver,'#accordianContainer > div > div:nth-child(3) > div > div > p')
        self.fifth_element_on_page_accordion = WebElement(driver,'#accordianContainer > div > div:nth-child(2) > div > div > p:nth-child(2)')

