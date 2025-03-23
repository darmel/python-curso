import requests
from assertpy.assertpy import assert_that

from json import dumps
from .print_helpers import pretty_print


def db_cleaner():
    id = 4
    while id < 100:
        url = 'http://127.0.0.1:5000/api/people/'
        respose = requests.delete(f'{url}/{id}')
        # print(respose)
        # if respose.status_code == 200:
        # body = respose.text()
        # print(respose.text)
        id = id + 1
        # print(id)


# db_cleaner()
