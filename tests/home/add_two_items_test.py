import unittest
from pages.home.decor_home_page import DecorHome
from pages.home.decor_orange_recliner_chair_page import DecorOrangeReclinerChair
from pages.home.decor_cart_page import DecorCart
from utilities.teststatus import TestStatus
from utilities.read_csv import getCSVData
from ddt import ddt, data, unpack
import pytest

@pytest.mark.usefixtures('oneTimeSetUp', 'setUp')
@ddt
class AddTwoItemsTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self):
        self.dh = DecorHome(self.driver)
        self.dorc = DecorOrangeReclinerChair(self.driver)
        self.dc = DecorCart(self.driver)
        self.ts = TestStatus(self.driver)

    #@data(*getCSVData('C:\\Users\\TT\\PycharmProjects\\Selenium-Skyscanner\\search_tickets_test_data.csv'))
    #@unpack
    def test_search_products(self):
        self.dh.search_orange_recliner_chair()
        result = self.dh.products_cat()
        self.ts.markFinal('SearchProductsTest', result)