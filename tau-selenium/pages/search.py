"""
Este modulo contiene la página de dudkdudkgo Search page
el page object para la pagina iniicial de busqueda
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class DuckDuckGoSearchPage:

    # URL
    URL = 'https://www.duckduckgo.com'

    # locators
    SEARCH_INPUT = (By.ID, 'searchbox_input')

    # Initializer
    # el init method es el constructor
    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def search(self, phrase):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(phrase + Keys.RETURN)
