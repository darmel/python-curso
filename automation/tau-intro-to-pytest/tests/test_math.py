
import pytest


@pytest.mark.math
def test_one_plus_one():  # cada test es una funcion, debe comenzar con "test_"
    assert 1+1 == 2


def test_one_plus_two():
    a = 1
    b = 2
    c = 3
    assert a+b == c


@pytest.mark.math
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError) as e:
        num = 1/0

    assert 'division by zero' in str(e.value)


# Parameterized

# tests for multiplication:
# two positive integers
# identity, multiply by 1
# zero: multiply by 0
# positive by negative
# negative by negative
# floats

# tuplas, usar una tupla por cada posible test
products = [
    (2, 3, 6),
    (1, 99, 99),
    (0, 99, 0),
    (3, -4, -12),
    (-5, -5, 25),
    (2.5, 6.7, 16.75)
]

# un decorator para ser marker


@pytest.mark.math
# un decorator para usar los parametrosq
@pytest.mark.parametrize('a,b,product', products)
def test_multiplication(a, b, product):
    assert a*b == product


# Si tengo fallas/errores en la importación...
# comrpobar que el $PYTHONPATH este seteado al root del proyecto
