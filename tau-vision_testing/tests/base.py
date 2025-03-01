# test poara checkear config de pytest
# def test_test():
#    a = 1
#    b = 2
#    assert a+b == 3

from config.base import APPLITOOLS_API_KEY
from unittest import TestCase

from selenium import webdriver

from applitools.selenium import Eyes


class baseTest(TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.initialize_eyes()
        self.driver.get('https://applitools.com/helloworld')

    def tearDown(self):
        self.driver.quit()

    def initialize_eyes(self):
        self.eyes = Eyes()
        self.eyes.api_key = APPLITOOLS_API_KEY
        return self.eyes
