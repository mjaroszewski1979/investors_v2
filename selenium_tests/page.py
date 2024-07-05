# Import WebDriverWait class with alias W
from selenium.webdriver.support.ui import WebDriverWait as W
# Import expected_conditions class with alias EC
from selenium.webdriver.support import expected_conditions as EC

# Import locators from the local module
from .locators import IndexPageLocators

class BasePage(object):
    """
    Base page class containing common actions performed on web pages.
    """

    def __init__(self, driver):
        # Initialize with a web driver instance
        self.driver = driver

    def do_clear(self, locator):
        # Wait for element to be visible and clear its contents
        W(self.driver, 10).until(EC.visibility_of_element_located(locator)).clear()

    def do_click(self, locator):
        # Wait for element to be visible and click it
        W(self.driver, 10).until(EC.visibility_of_element_located(locator)).click()

    def move_to_element(self, locator):
        # Wait for element to be visible and scroll to its location
        W(self.driver, 10).until(EC.visibility_of_element_located(locator)).location_once_scrolled_into_view

    def do_submit(self, locator):
        # Wait for element to be visible and submit it
        W(self.driver, 10).until(EC.visibility_of_element_located(locator)).submit()

    def do_send_keys(self, locator, text):
        # Wait for element to be visible and send text input to it
        W(self.driver, 10).until(EC.visibility_of_element_located(locator)).send_keys(text)

    def get_element(self, locator):
        # Wait for element to be visible and return it
        element = W(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return element

    def get_elements(self, locator):
        # Wait for all elements to be visible and return them
        elements = W(self.driver, 10).until(EC.visibility_of_all_elements_located(locator))
        return elements

    def get_element_text(self, locator):
        # Wait for element to be visible and return its text
        element = W(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return element.text

    def select_value(self, locator):
        # Wait for element to be visible and submit it
        W(self.driver, 10).until(EC.visibility_of_element_located(locator)).submit()

    def is_select_value_works(self, select_value, text):
        """
        Check if the select value functionality works as expected
        """

        # Scroll to select value element
        self.move_to_element(select_value)
        
        # Click on select value element
        self.do_click(select_value)
        
        # Click the submit button
        self.do_click(IndexPageLocators.SUBMIT_BUTTON)

        # Scroll to table data element
        self.move_to_element(IndexPageLocators.TABLE_DATA)

        # Get text of the investor name element
        data = self.get_element_text(IndexPageLocators.INVESTOR_NAME)

        # Return True if text is found in the data, else False
        return text in data


class IndexPage(BasePage):
    """
    Page object model for the Index Page containing methods to interact with the page elements.
    """

    def is_title_matches(self):
        # Check if the title of the page matches the expected title
        return 'Famous Investors' in self.driver.title

    def is_index_heading_displayed_correctly(self):
        # Verify if the index heading is displayed correctly
        index_heading = self.get_element_text(IndexPageLocators.INDEX_HEADING)
        text = 'TIME IS YOUR FRIEND; IMPULSE IS YOUR ENEMY.'
        return text in index_heading

    def is_country_select_works(self):
        # Verify if the country select functionality works as expected
        result = self.is_select_value_works(select_value=IndexPageLocators.COUNTRY_SELECT, text='MICHEL MORVAN')
        return result

    def is_market_select_works(self):
        # Verify if the market select functionality works as expected
        result = self.is_select_value_works(select_value=IndexPageLocators.MARKET_SELECT, text='MORTIMER J. BUCKLEY')
        return result

    def is_aum_select_works(self):
        # Verify if the AUM select functionality works as expected
        result = self.is_select_value_works(select_value=IndexPageLocators.AUM_SELECT, text='MORTIMER J. BUCKLEY')
        return result






