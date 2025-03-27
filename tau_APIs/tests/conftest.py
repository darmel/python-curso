import pytest
from clients.people_client import PeopleClient
from utils.helpers import db_cleaner
from utils.helpers import read_file
import random


@pytest.fixture
def client():
    return PeopleClient()


@pytest.fixture
def create_data():
    payload = read_file('create_person.json')
    random_no = random.randint(0, 1000)
    last_name = f'Lastname{random_no}'
    payload['lname'] = last_name
    yield payload


def pytest_sessionfinish(session, exitstatus):
    print("\nLimpiando la base de datos después de todas las pruebas...")
    db_cleaner()
    print("Limpieza completada.")
