import pytest

from stuff.accum import Accumulator

# func para usar fixture, fixture es una funcion
# un fixture siempre devulve algo
# pytest se encarga de buscar el fixture que matchee con el parametro de la funcion test


@pytest.fixture
def accum():
    return Accumulator()


# en lugar de crear un objeto en cada test, uso fixture como parametro del test
def test_acuumulator_init(accum):
    # accum = Accumulator()
    assert accum.count == 0


@pytest.mark.accumulator
def test_accumulator_add_one(accum):
    # accum = Accumulator()
    accum.add()
    assert accum.count == 1


@pytest.mark.accumulator
def test_accumulator_add_three():
    accum = Accumulator()
    accum.add(3)
    assert accum.count == 3


@pytest.mark.accumulator
def test_accumulator_add_twice():
    accum = Accumulator()
    accum.add()
    accum.add()
    assert accum.count == 2


def test_accumulator_cannot_set_count_directly():
    accum = Accumulator()
    with pytest.raises(AttributeError, match=r"can't set attribute") as e:
        accum.count = 10
