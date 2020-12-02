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
    _item_name = 'product-name' #class
    _item_price = '//td[@class="product-price"]//span[@class="woocommerce-Price-amount amount"]'
    _total_price = '//td[@data-title="Total"]//span[@class="woocommerce-Price-amount amount"]'
    _minus_button = 'minus' #class
    _update_cart_button = 'update_cart' #name
    _x_button = 'remove' #class
    _undo_button = 'restore-item' #class (wait for element before this?)
    _checkout_button = 'wc-proceed-to-checkout' #class
    _cart_updated_info = 'woocommerce-message' #class

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

    def click_minus_button(self):
        self.elementClick(self._minus_button, 'class')

    def click_update_cart(self):
        self.elementClick(self._update_cart_button, 'name')

    def click_x_button(self):
        self.elementClick(self._x_button, 'class')

    def click_undo_button(self):
        self.elementClick(self._undo_button, 'class')

    def click_checkout_button(self):
        self.elementClick(self._checkout_button, 'class')

    def card_updated_info_check(self):
        self.isElementPresent(self._cart_updated_info, 'class')

    def wait_for_undo_button(self):
        self.waitForElement(self._undo_button, locatorType='class')

    def wait_for_checkout_button(self):
        self.waitForElement(self._checkout_button, 'class')

    def get_cart_item_name(self):
        cart_item_name = self.getText(self._item_name, 'class')
        return cart_item_name

    def verify_prices(self):
        if self.sum_item_prices() == self.total_price():
            return True
        else:
            return False

    def proceed_with_checkout(self):
        cart_item_name = self.get_cart_item_name()
        self.click_minus_button()
        self.click_update_cart()
        self.card_updated_info_check()
        self.click_x_button()
        self.wait_for_undo_button()
        self.click_undo_button()
        self.wait_for_checkout_button()
        self.click_checkout_button()

        return cart_item_name