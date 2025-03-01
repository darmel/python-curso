from assertpy import assert_that
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from applitools.selenium import Eyes, Target
from applitools.selenium import AccessibilityRegion

from conftest import *
# from pages_objects.search_page import SearchPage


from selenium.webdriver import Chrome
from applitools.selenium import Eyes, Target
from selenium.webdriver.common.by import By

from applitools.selenium import Eyes, Target
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from applitools.selenium.fluent import SeleniumCheckSettings
from applitools.selenium.fluent import selenium_check_settings
from applitools.selenium import AccessibilityRegion
from applitools.selenium import AccessibilityGuidelinesVersion
from applitools.selenium import AccessibilityLevel
from applitools.selenium import AccessibilityRegionByRectangle
from applitools.selenium import AccessibilityRegionType
from applitools.selenium import AccessibilitySettings


APP_UNDER_TEST = 'https://automationbookstore.dev/'


# pytest maneja que si hay argumentos, va a fijarse en los fixtures del conftest


def test_filter_book_own(eyes: Eyes, driver: Chrome):
    driver.get(APP_UNDER_TEST)
    element = driver.find_element(By.ID, 'searchBar')

    element.send_keys('test')
    # Agile testing
    # java
    # test
    eyes.check(Target.window().fully().with_name("results page").layout())

    # eyes.check(Target.window().accessibility(
    #   By.ID, 'searchBar', AccessibilityRegionType.RegularText))

   # eyes.check(Target.window().fully().accessibility(
    #  By.TAG_NAME, 'body', AccessibilityRegionType.BoldText))
    # eyes.check(Target.frame(By.ID, 'searchBar'))

    # page.filter_books('Agile')
    # result = page.verify_visible_books_by_title('Agile Testing')
    # assert_that(result).is_equal_to(True)
    # eyes.check(Target.window().fully().with_name("Book Filter"))
