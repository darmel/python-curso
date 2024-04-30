import pytest
import re

from playwright.sync_api import Page, expect


@pytest.mark.ui
@pytest.mark.acme_bank
# usa page fixture, que lo provee el plugin de playwright
def test_acme_bank_login(page: Page):
    # Arrange:
    page.goto('https://demo.applitools.com')

    # Act:
    page.locator('id=username').fill('Dario')
    page.locator('id=password').fill('Admin123')
    page.locator('id=log-in').click()

    # Assert
    expect(page.locator('div.logo-w')).to_be_visible()
   # expect(page.locator('ul.main-manu')).to_be_visible()
    expect(page.get_by_text('Add Account')).to_be_visible()
    expect(page.get_by_text('Make Payment')).to_be_visible()
    expect(page.get_by_text('View Statement')).to_be_visible()
    expect(page.get_by_text('Request Increase')).to_be_visible()
    expect(page.get_by_text('Pay Now')).to_be_visible()


# para instalar playwright en python:
# $ pip install playwright
# para instalar la libreria para usarlo con pytest:
# $pip install pytest-playwright
# para instalar playwright propiamente dicho:
# $playwright install

# para corrrer los tests en forma headless:
# $ python -m pytest tests/test_ui.py
# para correr los tests y ver el browser,a demas hacerlo con pausas por cada interaccion:
# $ python -m pytest tests/test_ui.py --headed --slowmo 1000
