from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging
import time

class DecorHome(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #locators
    _search_button = '//button[@value="Search"]'
    _product_cat_label = '//h2[contains(text(), "Product categories")]'

    def click_search_button(self):
        self.elementClick(self._search_button, 'xpath')

    def products_cat(self):
        result = self.isElementPresent(self._product_cat_label, 'xpath')
        return result

    def search_products(self):
        self.click_search_button()