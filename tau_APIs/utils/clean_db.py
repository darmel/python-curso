import requests
from assertpy.assertpy import assert_that

from json import dumps
from .print_helpers import pretty_print


def db_cleaner():
    id = 4
    while id < 100:
        url = 'http://127.0.0.1:5000/api/people/'
        respose = requests.delete(f'{url}/{id}')
        id = id + 1
