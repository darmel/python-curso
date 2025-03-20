import requests
from utils.response import Response


class APIRequest:
    def get(self, url):
        response = requests.get(url)
        return self.__get_responses(response)

    def post(self, url, payload):
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        response = requests.post(url, data=payload, headers=headers)
        return self.__get_responses(response)

    def delete(self, url):
        response = requests.delete(url)
        return self.__get_responses(response)

    def __get_responses(self, response):
        return Response(
            status_code=response.status_code,
            text=response.text
            as_dict=response.json() if response.content else {},
            headers=response.headers
        )
