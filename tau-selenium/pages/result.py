"""
Este modulo contiene la página de dudkdudkgo Reslts page
el page object para la pagina de resultados
"""

from selenium.webdriver.common.by import By


class DuckDuckGoResultPage:

    # locators:
    # RESULT_LINK = (By.CSS_SELECTOR, 'react-results--main')
    RESULT_LINKS = (
        By.XPATH, "//article[contains(@id, 'r1-')]//span[contains(@class, 'EKtkFWMYpwzMKOYr0GYm') and contains(@class, 'LQVY1Jpkk8nyJ6HBWKAk')]")
    # RESULT_LINK = (By.CSS_SELECTOR, 'a.result__a')
    SEARCH_INPUT = (By.ID, 'search_form_input')

    # Initializer
    def __init__(self, browser):
        self.browser = browser

    # Interactions Methods

    # lista de los enlaces de los resultados como tesxto
    def result_link_titles(self):
        links = self.browser.find_elements(*self.RESULT_LINKS)
        titles = [link.text for link in links]
        return titles

    def search_input_value(self):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        value = search_input.get_attribute('value')
        return value

    def title(self):
        return self.browser.title
