"""
esto es el test de una busqueda en duckduckgo
"""

# importo las page object de las paginas que voy a usar
from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage
import pytest


@pytest.mark.parametrize('phrase', ['panda', 'python', 'polar bear'])
# el test usa como argumento a la funcion que maneja la instancia del webdriver
# pytest maneja que si hay argumentos, va a fijarse en los fixtures
def test_basic_duckduckgo_search(browser, phrase):

    # creo los dos objetos de las paginas que voy a usar
    search_page = DuckDuckGoSearchPage(browser)
    result_page = DuckDuckGoResultPage(browser)
    # PHRASE = "PANDA" deprecado porque ahora uso el decorator para parametrizar

    # Given la pagina de duckduckgo esta activa
    search_page.load()
    print("pagina cargada")

    # WHEN el user busca por "panda"
    search_page.search(phrase)

    # THEN el titulo de la pagina de resultados contiene "panda"
    assert phrase in result_page.title()

    # AND el valor de busqueda es "panda"
    assert phrase == result_page.search_input_value()

    # AND los enlaces de los resultados contiene "panda"
    titles = result_page.result_link_titles()
    print("titulos")
    print(titles)
    matches = [t for t in titles if phrase.lower() in t.lower()]
    assert len(matches) > 0
