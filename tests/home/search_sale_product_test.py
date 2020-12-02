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
        self.dh.search_sale_item()
        self.ds.buy_sale_item()
        self.dc.proceed_with_checkout()
        self.dch.place_order('Tomek', 'T', 'PL', 'Poleczki', '01-123', 'Warsaw', '555222111', 'email@email.com')

        # chair_title = self.dorc.verify_text_orange_recliner_chair('Orange Recliner with Leg Rest')
        # self.ts.mark(chair_title, 'Chair title')
        # self.dorc.buy_orange_recliner_chair(450)
        # self.dh.search_wooden_chair()
        # total_price = self.dc.verify_prices()
        # self.ts.markFinal('test_search_products', total_price)