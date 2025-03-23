import json
from uuid import uuid4
from utils.request import APIRequest
from config import BASE_URL


class PeopleClient:
    def __init__(self):
        self.base_url = BASE_URL
        self.request = APIRequest()

    def create_person(self, body=None):
        unique_last_name, response = self.__create_person_with_unique_last_name(
            body)
        return unique_last_name, response

    def __create_person_with_unique_last_name(self, body=None):
        if body is None:
            unique_last_name = f'Last-name{str(uuid4())}'
            payload = json.dumps({
                'fname': 'New_user',
                'lname': unique_last_name
            })
        else:
            unique_last_name = body['lname']
            payload = json.dumps(body)

        response = self.request.post(self.base_url, payload)
        return unique_last_name, response

    def read_all_persons(self):
        return self.request.get(self.base_url)

    def delete_person(self, person_id):
        url = f'{self.base_url}/{person_id}'
        return self.request.delete(url)

    def get_one_person(self, person_id):
        url = f'{self.base_url}/{person_id}'
        return self.request.get(url)
