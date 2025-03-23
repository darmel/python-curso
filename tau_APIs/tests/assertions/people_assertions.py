from assertpy.assertpy import assert_that, soft_assertions
import pytest
from cerberus import Validator


def assert_status_code(response, expected_code):
    assert_that(response.status_code).is_equal_to(expected_code)


def assert_fname_is_present(response, fname):
    first_names = [person['fname'] for person in response.as_dict]
    assert_that(first_names).contains(fname)


def assert_lname_is_present(response, lname):
    last_names = [person['lname'] for person in response.as_dict]
    assert_that(last_names).contains(lname)


def assert_one_person_has_expected_schema(schema, response):
    validator = Validator(schema, require_all=True)
    is_valid = validator.validate(response.as_dict)
    assert_that(is_valid, description=validator.errors).is_true()


def assert_all_has_expected_schema(schema, response):
    with soft_assertions():
        for person in response:
            assert_one_person_has_expected_schema(schema, person)
