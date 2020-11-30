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
    #_product_cat_label = '//h2[contains(text(), "Product categories")]'
    _search_button = '//button[@value="Search"]'
    _orange_recliner_chair = '//h2[contains(text(), "Orange Recliner")]'
    _wooden_rocking_chair_quick_view = '//a[@data-product_id="273"]'
    _main_page_logo = 'custom-logo' #class
    _close_quick_view = 'ast-quick-view-close' #id
    _shopping_cart_button = 'ast-cart-menu-wrap' #class


    def click_search_button(self):
        self.elementClick(self._search_button, 'xpath')

    # def products_cat(self):
    #     result = self.isElementPresent(self._product_cat_label, 'xpath')
    #     return result

    def scroll_down(self):
        self.webScroll('down')

    def scroll_up(self):
        self.webScroll('up')

    def click_orange_recliner_chair(self):
        self.elementClick(self._orange_recliner_chair, 'xpath')

    def click_wooden_rocking_chair_quick_view(self):
        self.elementClick(self._wooden_rocking_chair_quick_view, 'xpath')


    def search_products(self):
        self.scroll_down()
        self.click_orange_recliner_chair()

