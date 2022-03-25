from selenium.webdriver.common.by import By

class IndexPageLocators(object):
    
    INDEX_HEADING = (By.XPATH, "//div[@id='wrapper']//section[@class='intro']//header//p")
    ARROW_SCROLLY = (By.CLASS_NAME, 'arrow')
    COUNTRY_SELECT = (By.XPATH, "//select[@name='country-list']/option[@value='france']")
    MARKET_SELECT = (By.XPATH, "//select[@name='market-list']/option[@value='stocks']")
    AUM_SELECT = (By.XPATH, "//select[@name='aum-avg']/option[@value='above']")
    SUBMIT_BUTTON = (By.CLASS_NAME, 'primary')
    TABLE_DATA = (By.XPATH, "//table[@class='alt']//tbody//tr//td")
    INVESTOR_NAME = (By.CLASS_NAME, 'investor-name')


