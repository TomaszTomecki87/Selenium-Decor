import unittest
from pages.home.decor_home import DecorHome
from utilities.teststatus import TestStatus
from utilities.read_csv import getCSVData
from ddt import ddt, data, unpack
import pytest

@pytest.mark.usefixtures('oneTimeSetUp', 'setUp')
@ddt
class SearchProductsTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self):
        self.dc = DecorHome(self.driver)
        self.ts = TestStatus(self.driver)

    #@data(*getCSVData('C:\\Users\\TT\\PycharmProjects\\Selenium-Skyscanner\\search_tickets_test_data.csv'))
    #@unpack
    def test_search_products(self):
        self.dc.search_products()
        result = self.dc.products_cat()
        self.ts.markFinal('SearchProductsTest', result)