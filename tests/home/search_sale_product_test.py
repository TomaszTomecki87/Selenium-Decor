import unittest
from pages.home.decor_home_page import DecorHome
from pages.home.decor_sale_article_page import DecorSale
from pages.home.decor_cart_page import DecorCart
from pages.home.decor_checkout_page import DecorCheckout
from utilities.teststatus import TestStatus
from utilities.read_csv import getCSVData
from ddt import ddt, data, unpack
import pytest

@pytest.mark.usefixtures('oneTimeSetUp', 'setUp')
@ddt
class SearchSaleProductTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self):
        self.dh = DecorHome(self.driver)
        self.ds = DecorSale(self.driver)
        self.dc = DecorCart(self.driver)
        self.dch = DecorCheckout(self.driver)
        self.ts = TestStatus(self.driver)

    @data(*getCSVData('C:\\Users\\TT\\PycharmProjects\\Selenium-Decor\\search_sale_product_test_data.csv'))
    @unpack
    def test_search_sale_product(self, firstName, lastName, country, address, postcode, town, phone, email):
        self.dh.log.info('Start TEST Search Sale Product!!!')
        home_page_sale_mark = self.dh.verify_sale_mark()
        self.ts.mark(home_page_sale_mark, 'Sale mark present on home page')
        self.dh.search_sale_item()
        item_page_sale_mark = self.ds.verify_sale_mark()
        self.ts.mark(item_page_sale_mark, 'Sale mark present on item page')
        self.ds.buy_sale_item()
        cart_item_name = self.dc.get_cart_item_name()
        self.ts.mark(cart_item_name, 'Cart item name')
        self.dc.proceed_with_checkout()
        checkout_item_name = self.dch.get_checkout_item_name()
        formatted_checkout_item_name = checkout_item_name[:len(cart_item_name)]
        self.ts.mark(checkout_item_name, 'Checkout item name')
        self.dch.place_order(firstName, lastName, country, address, postcode, town, phone, email)
        invalid_payment_info = self.dch.verify_invalid_payment_info()
        self.ts.mark(invalid_payment_info, 'Invalid Payment Info present')
        test_search_sale_product_result = (cart_item_name == formatted_checkout_item_name)
        self.ts.markFinal('Test_search_sale_product', test_search_sale_product_result)
        self.driver.delete_all_cookies()
        self.driver.get('https://letskodeit.com/automationpractice/')