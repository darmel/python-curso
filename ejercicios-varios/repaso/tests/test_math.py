# repaso de pytest
# crear virtual evironment: python3 -m venv venv_pytest
# iniciar virtual envirnment: source venv_pytest/bin/activate
# instalar pytest: pip install pytest

import pytest
# los tests deben comenzar con test_ y usar assert
# test de ejemplo


@pytest.mark.math
def test_suma():
    assert 2 + 2 == 4


@pytest.mark.math
def test_one_plus_two():
    a = 1
    b = 2
    c = 3
    assert a + b == c


@pytest.mark.math
# como manejar exepciones
def test_devide_by_zero():
    with pytest.raises(ZeroDivisionError) as e:
        num = 1/0
    assert 'division by zero' in str(e.value)

# Parametrizar tests
# pytest mark prametrizer

#
# 2 positivos
# multipliucar por 1 (identidad)
# multiplicar por 0
# positivo por negativo
# negativo por negativo
# decimales


# se parametriza con una lista de tupla
products = [
    (2, 3, 6),
    (1, 99, 99),
    (0, 99, 0),
    (3, -4, -12),
    (-1, -5, 5),
    (2.5, 6.7, 16.75)
]

# esto es un decorador de la funcion, un decorador es una funcon que wrapea otra funcion
# el decorador tiene argumentos tambien.


@pytest.mark.math
@pytest.mark.parametrize('a, b, product', products)
def test_multiplication(a, b, product):
    assert a * b == product
