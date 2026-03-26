from selenium.common.exceptions import NoSuchElementException
from pages.base_page import BasePage

class DemoSite(BasePage):

    def exist_text_in_footer(self):
        try:
            self.find_element(locator='#root > footer > span') == '© 2013-2026 TOOLSQA.COM | ALL RIGHTS RESERVED.'
        except NoSuchElementException:
            return False
        return True

    def  click_elements_button(self):
        self.find_element(locator='#root > div > div > div.home-body > div > a:nth-child(1) > div > div').click()

    def exist_text_in_mid(self):
        try:
            self.find_element(locator='#root > div > div > div > div.col-12.mt-4.col-md-6.col-xl-7') == 'Please select an item from left to start practice.'
        except NoSuchElementException:
            return False
        return True