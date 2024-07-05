# Import the 'time' module for time-related functions
import time
# Import the webdriver module from Selenium for web browser automation
from selenium import webdriver

# Import the StaticLiveServerTestCase class for testing Django static files
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
# Import the 'reverse' function for URL reversing
from django.urls import reverse

# Import the 'models' module from the 'investors' app
from investors import models
# Import the 'page' module from the current package
from . import page


class InvestorsTest(StaticLiveServerTestCase):
    """
    Test case for Investors using Selenium WebDriver.
    Includes setup and teardown methods, and tests for the Index page.
    """

    def setUp(self):
        # Initialize the Chrome WebDriver
        self.driver =  webdriver.Chrome('selenium_tests/chromedriver.exe')
        self.driver.set_window_size(1920, 1080)

        # Create and save country instances
        self.country_1 = models.Country(name='united states', population=300000000)
        self.country_1.save()
        self.country_2 = models.Country(name='france', population=50000000)
        self.country_2.save()

        # Create and save fund instances
        self.fund_1 = models.Fund(name='the vanguard group', aum=300000000, long=True, market='stocks')
        self.fund_1.save()
        self.fund_2 = models.Fund(name='sesamm', aum=100000000, long=False, market='bonds')
        self.fund_2.save()

        # Create and save investor instances
        self.investor_1 = models.Investor(name='MORTIMER J. BUCKLEY', age='1990-10-10', country=self.country_1, fund=self.fund_1)
        self.investor_1.save()
        self.investor_2 = models.Investor(name='MICHEL MORVAN', age='1980-10-10', country=self.country_2, fund=self.fund_2)
        self.investor_2.save()

    def tearDown(self):
        # Close the WebDriver
        self.driver.close()


    def test_indexpage(self):
        # Navigate to the live server URL
        self.driver.get(self.live_server_url)

        # Initialize the IndexPage object
        index_page = page.IndexPage(self.driver)

        # Assert that the page title matches the expected title
        assert index_page.is_title_matches()

        # Assert that the index heading is displayed correctly
        assert index_page.is_index_heading_displayed_correctly()

        # Assert that the country select functionality works
        assert index_page.is_country_select_works()

        # Assert that the market select functionality works
        assert index_page.is_market_select_works()

        # Assert that the AUM select functionality works
        assert index_page.is_aum_select_works()

  




        

    
