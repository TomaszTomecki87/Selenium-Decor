from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging
import time

class DecorCheckout(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #locators
    _first_name = 'billing_first_name' #id
    _last_name = 'billing_last_name' #id
    _country = 'billing_country' #id - dropdown list
    _street_address = 'billing_address_1' #id
    _town = 'billing_city' #id
    _postcode = 'billing_postcode' #id
    _phone = 'billing_phone' #id
    _email = 'billing_email' #id
    _item_name = 'product-name' #class
    _place_order = 'place_order' #id
    _invalid_payment_info = 'woocommerce_error' #class

    def get_checkout_item_name(self):
        checkout_item_name = self.getText(self._item_name, 'class')
        return checkout_item_name

    def enter_first_name(self, firstName):
        self.sendKeys(firstName, self._first_name)

    def enter_last_name(self, lastName):
        self.sendKeys(lastName, self._last_name)

    def select_country(self, country):
        self.click_from_dropdown(self._country, value=country)

    def enter_street_address(self, streetAddress):
        self.sendKeys(streetAddress, self._street_address)

    def enter_postcode(self, postcode):
        self.sendKeys(postcode, self._postcode)

    def enter_town(self, town):
        self.sendKeys(town, self._town)

    def enter_phone(self, phone):
        self.sendKeys(phone, self._phone)

    def enter_email(self, email):
        self.sendKeys(email, self._email)

    def click_place_order(self):
        self.elementClick(self._place_order)

    def verify_invalid_payment_info(self):
        payment_error = self.getText(self._invalid_payment_info, 'class')
        return payment_error


    def place_order(self, firstName, lastName, country, streetAddress,postcode, town, phone, email):
        checkout_item_name = self.get_checkout_item_name()
        self.enter_first_name(firstName)
        self.enter_last_name(lastName)
        self.select_country(country)
        time.sleep(5)
        self.enter_street_address(streetAddress)
        self.enter_postcode(postcode)
        self.enter_town(town)
        self.enter_phone(phone)
        self.enter_email(email)
        self.click_place_order()
        time.sleep(5)

        return checkout_item_name