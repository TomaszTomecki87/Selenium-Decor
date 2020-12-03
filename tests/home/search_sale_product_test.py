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

    #@data(*getCSVData('C:\\Users\\TT\\PycharmProjects\\Selenium-Skyscanner\\search_tickets_test_data.csv'))
    #@unpack
    def test_search_sale_product(self):
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
        self.ts.mark(checkout_item_name, 'Checkout item name')
        self.dch.place_order('Tomek', 'T', 'PL', 'Poleczki', '01-123', 'Warsaw', '555222111', 'email@email.com')
        invalid_payment_info = self.dch.verify_invalid_payment_info()
        self.ts.mark(invalid_payment_info, 'Invalid Payment Info present')
        #self.ts.markFinal('Test_search_sale_product', )



        # self.ts.markFinal('test_search_products', total_price)