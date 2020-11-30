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

    def sum_item_prices(self):
        prices = []
        items_price_list = self.getElementList(self._item_price, 'xpath')
        self.log.info(items_price_list)
        for i in items_price_list:
            text = self.getText(element=i)
            text = text[1:]
            text = int(float(text))
            self.log.info(text)
            prices.append(text)
        self.log.info(prices)
        price_sum = sum(prices)
        self.log.info(price_sum)
        return price_sum

    def total_price(self):
        total_price = self.getText(self._total_price, 'xpath')
        total_price = total_price[1:]
        total_price = int(float(total_price))
        self.log.info(total_price)
        return total_price

    def verify_prices(self):
        if self.sum_item_prices() == self.total_price():
            return True
        else:
            return False