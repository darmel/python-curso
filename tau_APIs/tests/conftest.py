import pytest
from clients.people_client import PeopleClient
from utils.clean_db import db_cleaner
from utils.file_reader import read_file
import random


@pytest.fixture
def client():
    return PeopleClient()


@pytest.fixture
def create_data():
    payload = read_file('create_person.json')
    # print("payload desde json:")
    # pretty_print(payload)
    random_no = random.randint(0, 1000)
    last_name = f'Lastname{random_no}'
    payload['lname'] = last_name
    # print("payload desde json pero modificada:")
    # pretty_print(payload)
    yield payload


def pytest_sessionfinish(session, exitstatus):
    print("\nLimpiando la base de datos después de todas las pruebas...")
    db_cleaner()
    print("Limpieza completada.")
