# Import the By class for locating elements
from selenium.webdriver.common.by import By

class IndexPageLocators(object):
    """
    Class to store locators for elements on the index page.
    Uses By class to define how elements are located.
    """

    # Locator for the index heading
    INDEX_HEADING = (By.XPATH, "//div[@id='wrapper']//section[@class='intro']//header//p")

    # Locator for the arrow scroll element
    ARROW_SCROLLY = (By.CLASS_NAME, 'arrow')

    # Locator for selecting the country 'France' from the dropdown
    COUNTRY_SELECT = (By.XPATH, "//select[@name='country-list']/option[@value='france']")

    # Locator for selecting 'stocks' from the market dropdown
    MARKET_SELECT = (By.XPATH, "//select[@name='market-list']/option[@value='stocks']")

    # Locator for selecting 'above' from the AUM dropdown
    AUM_SELECT = (By.XPATH, "//select[@name='aum-avg']/option[@value='above']")

    # Locator for the submit button
    SUBMIT_BUTTON = (By.CLASS_NAME, 'primary')

    # Locator for the table data elements
    TABLE_DATA = (By.XPATH, "//table[@class='alt']//tbody//tr//td")

    # Locator for the investor name elements
    INVESTOR_NAME = (By.CLASS_NAME, 'investor-name')


