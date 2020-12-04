import unittest
from tests.home.search_products_test import SearchProductsTests
from tests.home.search_sale_product_test import SearchSaleProductTest

#create TestCases
tc1 = unittest.TestLoader().loadTestsFromTestCase(SearchProductsTests)
tc2 = unittest.TestLoader().loadTestsFromTestCase(SearchSaleProductTest)

#create TestSuit
ts1 = unittest.TestSuite([tc1, tc2])

unittest.TextTestRunner(verbosity=2).run(ts1)