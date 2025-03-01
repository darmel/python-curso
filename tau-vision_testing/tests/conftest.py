import pytest
import os

from applitools.selenium import *

from applitools.selenium import Eyes
from selenium import webdriver
from applitools.selenium import Eyes, Target
from applitools.selenium.fluent import SeleniumCheckSettings
from applitools.selenium import *
from applitools.selenium.runner import EyesRunner
from selenium.webdriver import Chrome, ChromeOptions, Remote
from config.base import APPLITOOLS_API_KEY


import os
import pytest

from applitools.selenium import *
from applitools.selenium.runner import EyesRunner
from selenium.webdriver import Chrome, ChromeOptions, Remote

APP_NAME = 'bookstore'
APP_UNDER_TEST = 'https://automationbookstore.dev/'
# inicia la instancia del webdriver


@pytest.fixture(scope='session')
def api_key():
    """
    agarra la api_key de una variable de entorno NO OLVIDAR CONFIGURAR
    """
    return os.getenv('APPLITOOLS_API_KEY')


@pytest.fixture(scope='session')
def headless():
    return 'false'


@pytest.fixture(scope='function')
def driver():
    driver = Chrome()
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def eyes(runner: EyesRunner):
    eyes = initialize_eyes(runner)
    yield eyes


def initialize_eyes(runner: EyesRunner):
    eyes = Eyes(runner)
    eyes.api_key = APPLITOOLS_API_KEY
    return eyes


@pytest.fixture(scope='session')
def runner():
    run = ClassicRunner()
    yield run


@pytest.fixture(scope='session')
def batch_info():
    runner_name = "Classic runner"
    return BatchInfo(f"test filter test")


@pytest.fixture(scope='session')
def configuration(api_key: str, batch_info: BatchInfo):

    # Construct the object
    # la class Configuration esta definida en la libreria
    config = Configuration().set_accessibility_validation(AccessibilitySettings(
        AccessibilityLevel.AAA, AccessibilityGuidelinesVersion.WCAG_2_1))

    # Set the batch for the config.
    config.set_batch(batch_info)

    # Set the Applitools API key so test results are uploaded to your account.
    # If you don't explicitly set the API key with this call,
    # then the SDK will automatically read the `APPLITOOLS_API_KEY` environment variable to fetch it.
    config.set_api_key(api_key)

    # Return the configuration object
    return config


@pytest.fixture(scope='function')
def eyes(
        runner: EyesRunner,
        configuration: Configuration,
        driver: Chrome,
        request: pytest.FixtureRequest):

    eyes = Eyes(runner)
    eyes.set_configuration(configuration)

    eyes.open(
        driver=driver,
        app_name='Book Filter',
        test_name=get_test_name(),
        #     test_name=request.node.name,
        viewport_size=RectangleSize(800, 600))

    yield eyes
    eyes.close_async()


# def validate_window(driver, eyes, tag):
#    open_eyes(driver, eyes)
#    eyes.check_window(tag=tag)
#    eyes.check(Target.window())
#    eyes.check(Target.window().fully().with_name("Book Filter"))
#    close_eyes(eyes)
#
#
# def open_eyes(driver, eyes):
#    eyes.open(driver, APP_NAME, test_name=get_test_name())
#
#
def get_test_name():
    import inspect
    return inspect.stack()[3].function
#
#
# def close_eyes(eyes):
#    eyes.close
