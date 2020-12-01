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
    _orange_recliner_chair = '//h2[contains(text(), "Orange Recliner")]'
    _wooden_rocking_chair_quick_view = '//a[@data-product_id="273"]'
    _main_page_logo = 'custom-logo' #class
    _close_quick_view = 'ast-quick-view-close' #id
    _shopping_cart_button = 'ast-cart-menu-wrap' #class
    _add_to_cart_button = 'add-to-cart'  # name
    _sale_mark = '//span[@class="onsale circle"]'
    _sale_mark_full_xpath = '//li[contains(@class, "ast-article-single")]//div[@class="astra-shop-thumbnail-wrap"]//span[@class="onsale circle"]'


    def click_search_button(self):
        self.elementClick(self._search_button, 'xpath')

    def scroll_down(self):
        self.webScroll('down')

    def scroll_up(self):
        self.webScroll('up')

    def click_orange_recliner_chair(self):
        self.elementClick(self._orange_recliner_chair, 'xpath')

    def click_wooden_rocking_chair_quick_view(self):
        self.elementClick(self._wooden_rocking_chair_quick_view, 'xpath')

    def add_to_cart(self):
        self.elementClick(self._add_to_cart_button, 'name')

    def close_quick_view(self):
        self.elementClick(self._close_quick_view, 'id')

    def shopping_cart(self):
        self.elementClick(self._shopping_cart_button, 'class')

    def sale_parent_element(self):
        self.click_parent_element(self._sale_mark, 'xpath')


    def search_orange_recliner_chair(self):
        self.scroll_down()
        self.click_orange_recliner_chair()

    def search_wooden_chair(self):
        self.scroll_down()
        self.click_wooden_rocking_chair_quick_view()
        self.add_to_cart()
        self.close_quick_view()
        self.scroll_up()
        self.shopping_cart()

    def search_sale_item(self):
        self.scroll_down()
        self.sale_parent_element()
