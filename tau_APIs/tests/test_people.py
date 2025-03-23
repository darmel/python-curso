# import random
import requests
from assertpy.assertpy import assert_that, soft_assertions
import pytest
# from json import dumps, loads
# import json
from pathlib import Path
# from utils.file_reader import read_file
from utils.print_helpers import pretty_print
# from config import BASE_URL
# from uuid import uuid4
from jsonpath_ng import parse
from tests.schema_test import schema
from cerberus import Validator

# from utils.request import APIRequest
# from utils.response import Response
from clients.people_client import PeopleClient
import tests.assertions.people_assertions as pa
from utils.helpers import obtain_person_by_lastname


def test_read_all_has_kent(client):
    response = client.read_all_persons()
    # print(people)
    # pretty_print(people) #na funcion creada en utils.print_helpers
    pa.assert_status_code(response, 200)
    # print(response.as_dict)
    pa.assert_fname_is_present(response, 'Kent')


def test_create_a_person(client):
    unique_last_name, respose = client.create_person()
    # assert_that(respose.status_code).is_equal_to(204)
    pa.assert_status_code(respose, 204)
    people = client.read_all_persons()
    new_user = obtain_person_by_lastname(unique_last_name, people.as_dict)
    assert_that(new_user).is_not_empty()
    # print(new_user)
    pa.assert_lname_is_present(people, unique_last_name)


def test_user_can_be_deleted(client):
    unique_last_name, response = client.create_person()
    pa.assert_status_code(response, 204)
    people = client.read_all_persons()
    new_user = obtain_person_by_lastname(unique_last_name, people.as_dict)
    # print("new user en deleted test")
    # pretty_print(new_user)
    # print()
    # print(f"id del new user {new_user[0]['person_id']}")
    id_person_to_be_deleted = new_user[0]['person_id']
    # print("id:_ ", id_person_to_be_deleted)
    response = client.delete_person(id_person_to_be_deleted)
    # pretty_print(response.text)
    pa.assert_status_code(response, 200)
    # unique_last_name = 'Farrell'  # para probar si el assert is empty falla.
    # vuelve a obtener people, para verificar que el new user no este.
    people = client.read_all_persons()
    new_user = obtain_person_by_lastname(
        unique_last_name, people.as_dict)
    # print(new_user)
    assert_that(new_user).is_empty()
    # pretty_print(response.text)


def test_person_added_with_json_template(client, create_data):
    _, response = client.create_person(create_data)
    # pretty_print(response)
    pa.assert_status_code(response, 204)
    people = client.read_all_persons()
    pa.assert_lname_is_present(people, create_data['lname'])

    # de esta forma es para usar jsonpath, usando: jsonpath-ng
    # $: emepznado en la raiz, [*]:todos los elementos del array, lname:lo que busco
    jsonpath_expr = parse("$.[*].lname")
    # print("jsonpath: ")
    # pretty_print(jsonpath_expr)
    persons_lnames = [match.value for match in jsonpath_expr.find(
        people.as_dict)]  # esto me devuelve un array de lnames
    # print("lnames: ")
    # pretty_print(persons_lnames)
    assert_that(persons_lnames).contains(create_data['lname'])


def test_read_one_person_has_expected_schema(client):
    response = client.get_one_person(1)
    # pretty_print(response.as_dict)
    pa.assert_status_code(response, 200)
    # creo un objeto "validator" de la clase Validator usando el schema definido
    # validator = Validator(schema, require_all=True)
    # uso el metodo validate que me dara true or false
    # is_valid = validator.validate(response.as_dict)
    # assert_that(is_valid, description=validator.errors).is_true()
    pa.assert_one_person_has_expected_schema(schema, response)


def test_read_all_has_expected_schema(client):
    # response = requests.get(f'{BASE_URL}')
    # people = json.loads(response.text)
    response = client.read_all_persons()
    # pretty_print(response.as_dict)
    # assert_that(response.status_code).is_equal_to(200)
    pa.assert_status_code(response, 200)
    people = response.as_dict
    # pretty_print(people)
    # uso de nuevo el objetor validador
    # validator = Validator(schema, require_all=True)
    # with soft_assertions():
    #    for person in people:  # hace la validacion para cada person en people
    #        is_valid = validator.validate(person)
    #        assert_that(is_valid, description=validator.errors).is_true()
    # pa.assert_all_has_expected_schema(schema, response)


# def obtain_person_by_lastname(unique_last_name, people):
#    return [person for person in people if person['lname']
#            == unique_last_name]  # new_user va a ser igual a person si lname == unique_last_name, y esto lo prueba para cada person en people
