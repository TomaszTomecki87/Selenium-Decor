from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging
import time

class DecorCart(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #locators
    _item_price = '//td[@class="product-price"]//span[@class="woocommerce-Price-amount amount"]'
    _total_price = '//td[@data-title="Total"]//span[@class="woocommerce-Price-amount amount"]'