import random
import requests
from assertpy.assertpy import assert_that
import pytest
from json import dumps, loads
import json
from pathlib import Path
from utils.file_reader import read_file
from utils.print_helpers import pretty_print
from config import BASE_URL
from uuid import uuid4
from jsonpath_ng import parse


def test_read_all_has_kent():
    respose, people = obtain_people()
    # print(people)
    # pretty_print(people) #na funcion creada en utils.print_helpers

    assert_that(respose.status_code).is_equal_to(200)
    first_names = [person['fname'] for person in people]
    assert_that(first_names).contains('Kent')


def test_create_a_person():
    # para crear un apellido unico
    unique_last_name, respose = create_new_unique_user()
    # el codigo de exito viene de la info de la API
    assert_that(respose.status_code).is_equal_to(204)

    _, people = obtain_people()
    new_user = obtain_person_by_lastname(unique_last_name, people)
    assert_that(new_user).is_not_empty()
    # print(new_user)
    assert_that(new_user[0]['lname']).is_equal_to(unique_last_name)


def test_user_can_be_deleted():
    unique_last_name, respose = create_new_unique_user()
    _, people = obtain_people()
    new_user = obtain_person_by_lastname(
        unique_last_name=unique_last_name, people=people)
    # print("new user en deleted test")
    # pretty_print(new_user)
    # print(new_user[0]['person_id'])
    person_to_be_deleted = new_user[0]['person_id']
    # print(person_to_be_deleted)
    respose = requests.delete(f'{BASE_URL}/{person_to_be_deleted}')
    # pretty_print(respose)
    assert_that(respose.status_code).is_equal_to(200)
    # unique_last_name = 'Farrell'  # para probar si el assert is empty falla.
    # vuelve a obtener people, para verificar que l new user no este.
    _, people = obtain_people()
    new_user = obtain_person_by_lastname(
        unique_last_name=unique_last_name, people=people)
    # print(new_user)
    assert_that(new_user).is_empty()
    # pretty_print(respose)


def test_person_added_with_json_template(create_data):
    create_new_unique_user(create_data)
    # pretty_print(create_data)

    response = requests.get(BASE_URL)
    assert_that(response.status_code).is_equal_to(200)
    people = loads(response.text)
    # asi se puede conseguir los assert igual que en los otros tests
    # new_user = obtain_person_by_lastname(create_data['lname'], people=people)
    # assert_that(new_user[0]['lname']).is_equal_to(create_data['lname'])

    # de esta forma es para usar jsonpath, usando: jsonpath-ng
    # $: emepznado en la raiz, [*]:todos los elementos del array, lname:lo que busco
    jsonpath_expr = parse("$.[*].lname")
    # print("jsonpath: ")
    # pretty_print(jsonpath_expr)
    persons_lnames = [match.value for match in jsonpath_expr.find(
        people)]  # esto me devuelve un array de lnames
    # print("lnames: ")
    # pretty_print(persons_lnames)
    assert_that(persons_lnames).contains(create_data['lname'])


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


def obtain_person_by_lastname(unique_last_name, people):
    return [person for person in people if person['lname']
            == unique_last_name]  # new_user va a ser igual a person si lname == unique_last_name, y esto lo prueba para cada person en people


def obtain_people():
    respose = requests.get(BASE_URL)
    people = respose.json()
    return respose, people


def create_new_unique_user(body=None):
    if body is None:
        unique_last_name = f'Last-name{str(uuid4())}'
        payload = dumps({
            'fname': 'New_user',
            'lname': unique_last_name
        })  # como crear la payload esta en la info de la API, y el dumps es para convertirlo en json
        # pretty_print(payload)
    else:
        unique_last_name = body['lname']
        payload = dumps(body)

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }  # como crear los headers tambein viene de la info de la API

    # pretty_print(headers)

    # como esta en orden no haria falta especificar, pero es mejor asi
    respose = requests.post(url=BASE_URL, data=payload, headers=headers)
    return unique_last_name, respose
