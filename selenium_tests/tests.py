from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from . import page
from investors import models
from django.urls import reverse
import time




class BitcoinTest(StaticLiveServerTestCase):

    def setUp(self):
        self.driver =  webdriver.Chrome('selenium_tests/chromedriver.exe')
        self.driver.set_window_size(1920, 1080)
        
        self.country_1 = models.Country(name='united states', population=300000000)
        self.country_1.save()
        self.country_2 = models.Country(name='france', population=50000000)
        self.country_2.save()
        self.fund_1 = models.Fund(name='the vanguard group', aum=300000000, long=True, market='stocks')
        self.fund_1.save()
        self.fund_2 = models.Fund(name='sesamm', aum=100000000, long=False, market='bonds')
        self.fund_2.save()
        self.investor_1 = models.Investor(name='MORTIMER J. BUCKLEY', age='1990-10-10', country=self.country_1, fund=self.fund_1)
        self.investor_1.save()
        self.investor_2 = models.Investor(name='MICHEL MORVAN', age='1980-10-10', country=self.country_2, fund=self.fund_2)
        self.investor_2.save()

    def tearDown(self):
        self.driver.close()


    def test_indexpage(self):
        self.driver.get(self.live_server_url)
        index_page = page.IndexPage(self.driver)
        assert index_page.is_title_matches()
        assert index_page.is_index_heading_displayed_correctly()
        assert index_page.is_country_select_works()
        assert index_page.is_market_select_works()
        assert index_page.is_aum_select_works()
  




        

    