from selenium.webdriver.support.ui import WebDriverWait as W
from selenium.webdriver.support import expected_conditions as EC
from .locators import IndexPageLocators







class BasePage(object):


    def __init__(self, driver):
        self.driver = driver

    def do_clear(self, locator):
        W(self.driver, 10).until(EC.visibility_of_element_located(locator)).clear()

    def do_click(self, locator):
        W(self.driver, 10).until(EC.visibility_of_element_located(locator)).click()

    def move_to_element(self, locator):
        W(self.driver, 10).until(EC.visibility_of_element_located(locator)).location_once_scrolled_into_view

    def do_submit(self, locator):
        W(self.driver, 10).until(EC.visibility_of_element_located(locator)).submit()

    def do_send_keys(self, locator, text):
        W(self.driver, 10).until(EC.visibility_of_element_located(locator)).send_keys(text)

    def get_element(self, locator):
        element = W(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return element

    def get_elements(self, locator):
        elements = W(self.driver, 10).until(EC.visibility_of_all_elements_located(locator))
        return elements

    def get_element_text(self, locator):
        element = W(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return element.text

    def select_value(self, locator):
        W(self.driver, 10).until(EC.visibility_of_element_located(locator)).submit()

    def is_select_value_works(self, select_value, text):
        self.move_to_element(select_value)
        self.do_click(select_value)
        self.do_click(IndexPageLocators.SUBMIT_BUTTON)
        self.move_to_element(IndexPageLocators.TABLE_DATA)
        data = self.get_element_text(IndexPageLocators.INVESTOR_NAME)
        return text in data





    


class IndexPage(BasePage):

    def is_title_matches(self):
        return 'Famous Investors' in self.driver.title

    def is_index_heading_displayed_correctly(self):
        index_heading = self.get_element_text(IndexPageLocators.INDEX_HEADING)
        text = 'TIME IS YOUR FRIEND; IMPULSE IS YOUR ENEMY.'
        return text in index_heading

    def is_country_select_works(self):
        result = self.is_select_value_works(select_value=IndexPageLocators.COUNTRY_SELECT, text='MICHEL MORVAN')
        return result

    def is_market_select_works(self):
        result = self.is_select_value_works(select_value=IndexPageLocators.MARKET_SELECT, text='MORTIMER J. BUCKLEY')
        return result

    def is_aum_select_works(self):
        result = self.is_select_value_works(select_value=IndexPageLocators.AUM_SELECT, text='MORTIMER J. BUCKLEY')
        return result






