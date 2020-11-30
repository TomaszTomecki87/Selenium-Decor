from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging
import time

class DecorOrangeReclinerChair(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #locators
    _orange_recliner_price = '//span[contains(@class, "woocommerce-Price-amount amount") and contains(text(), "419")]'
    _add_to_cart_button = 'add-to-cart'  # name
    _view_cart_button = '//a[@title="View cart"]'
    _main_page_logo = 'custom-logo'  # class
    _text = '//h1[contains(text(), "Orange Recliner with Leg Rest")]'
    #_title = 'product_title entry-title' #class

    def verify_text_orange_recliner_chair(self, item_name):
        text = self.getText(locator=self._text, locatorType='xpath')
        text = text.lower()
        item_name = item_name.lower()
        if text == item_name:
            return True
        else:
            return False


    def verify_price(self):
        price = self.getText(self._orange_recliner_price, 'xpath')
        price = price[1:]
        price = int(float(price))
        return price

    def add_to_cart(self):
        self.elementClick(self._add_to_cart_button, 'name')

    def view_cart_button(self):
        view_cart = self.isElementPresent(self._view_cart_button, 'xpath')
        return view_cart

    def return_to_main_page(self):
        self.elementClick(self._main_page_logo, 'class')

    def buy_on_price(self, price):
        if self.verify_price() < price:
            self.add_to_cart()
            is_visible = self.view_cart_button()
            if is_visible:
                self.log.info('View Cart button visible')
            else:
                self.log.info('View cart button NOT visible')
        else:
            self.return_to_main_page()

    def buy_orange_recliner_chair(self, price):
        self.buy_on_price(price)
        self.return_to_main_page()