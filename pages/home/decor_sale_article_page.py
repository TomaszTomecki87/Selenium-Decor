from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging
import time


class DecorSale(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #locators
    _plus_button = 'plus' #class
    _shopping_cart_button = 'ast-cart-menu-wrap'  # class
    _add_to_cart_button = 'add-to-cart'  # name
    _sale_mark = '//span[@class="onsale circle"]'

    def click_plus_button(self):
        self.elementClick(self._plus_button, 'class')

    def add_to_cart(self):
        self.elementClick(self._add_to_cart_button, 'name')

    def shopping_cart(self):
        self.elementClick(self._shopping_cart_button, 'class')

    def verify_sale_mark(self):
        element = self.getElement(self._sale_mark, 'xpath')
        return element


    def buy_sale_item(self):
        self.click_plus_button()
        self.add_to_cart()
        time.sleep(2)
        self.shopping_cart()