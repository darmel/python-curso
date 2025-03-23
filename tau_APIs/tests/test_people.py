from assertpy.assertpy import assert_that, soft_assertions
import pytest
from pathlib import Path
from jsonpath_ng import parse
from tests.schema_test import schema

import tests.assertions.people_assertions as pa
from utils.helpers import obtain_person_by_lastname


def test_read_all_has_kent(client):
    response = client.read_all_persons()
    pa.assert_status_code(response, 200)
    pa.assert_fname_is_present(response, 'Kent')


def test_create_a_person(client):
    unique_last_name, respose = client.create_person()
    pa.assert_status_code(respose, 204)
    people = client.read_all_persons()
    new_user = obtain_person_by_lastname(unique_last_name, people.as_dict)
    assert_that(new_user).is_not_empty()
    pa.assert_lname_is_present(people, unique_last_name)


def test_user_can_be_deleted(client):
    unique_last_name, response = client.create_person()
    pa.assert_status_code(response, 204)
    people = client.read_all_persons()
    new_user = obtain_person_by_lastname(unique_last_name, people.as_dict)
    id_person_to_be_deleted = new_user[0]['person_id']
    response = client.delete_person(id_person_to_be_deleted)
    pa.assert_status_code(response, 200)
    people = client.read_all_persons()
    new_user = obtain_person_by_lastname(
        unique_last_name, people.as_dict)
    assert_that(new_user).is_empty()


def test_person_added_with_json_template(client, create_data):
    _, response = client.create_person(create_data)
    pa.assert_status_code(response, 204)
    people = client.read_all_persons()
    pa.assert_lname_is_present(people, create_data['lname'])

    jsonpath_expr = parse("$.[*].lname")

    persons_lnames = [match.value for match in jsonpath_expr.find(
        people.as_dict)]
    assert_that(persons_lnames).contains(create_data['lname'])


def test_read_one_person_has_expected_schema(client):
    response = client.get_one_person(1)
    pa.assert_status_code(response, 200)
    pa.assert_one_person_has_expected_schema(schema, response)


def test_read_all_has_expected_schema(client):
    response = client.read_all_persons()
    pa.assert_status_code(response, 200)
    people = response.as_dict
