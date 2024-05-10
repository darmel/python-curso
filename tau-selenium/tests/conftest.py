"""
Este modulo contiene los fixtures para inciar y cerrar el driver
es necesario que este en el directorio tests
es necesario que se llame conftest

"""

import pytest
import selenium.webdriver
import json  # para leer el archivo de config.json


@pytest.fixture
def config(scope='sesion'):  # scope= sesion, es para que lo  lea una vez y no en cada test
    # lee el json
    with open('config.json') as config_file:
        config = json.load(config_file)

    # checkeamos los valores de la config
    assert config['browser'] in ['Firefox', 'Chrome', 'Headless Chrome']
    assert isinstance(config['implicit_wait'], int)
    assert config['implicit_wait'] > 0

    # si todo es valido, devolvemos la config
    return config


@pytest.fixture
def browser(config):  # ahora el browser recibe la config que ya fue checkeada
    # incializa una instancia del webdriver segun venga desde el config
    if config['browser'] == 'Firefox':
        b = selenium.webdriver.Firefox()
    elif config['browser'] == 'Chrome':
        b = selenium.webdriver.Chrome()
    elif config['browser'] == 'Headless Chrome':
        opts = selenium.webdriver.ChromeOptions()
        opts.add_argument('headless')
        b = selenium.webdriver.Chrome(options=opts)
    else:
        raise Exception(f'Browser "{config["browser"]}" is not supported')

    # define el tiempo de espera para que aparezcan los eleementos segun la config
    b.implicitly_wait(config['implicit_wait'])

    # devuvle la instancia de webdriver
    yield b

    # cuando regresa, cierra la instancia
    b.quit()


# quedo deprecado
# @pytest.fixture
# def browser():
#    # inicializa una instancia de chromedriver
#    b = selenium.webdriver.Chrome()
#
#    # genera una espera de HASTA 10 segundos para que se levante todo
#    b.implicitly_wait(10)
#
#    # devuelve la instancia del chromedriver
#    yield b
#
#    # no imporeta como le vaya al test, siempre vuelve a este punto
#    # cierra la instancia del webdriver para el cleanup
#    b.quit()
