import pytest
import requests


@pytest.mark.duckduckgo
@pytest.mark.api
def test_duckduckgo_instant_answer_api():
    # arange
    url = "http://api.duckduckgo.com/?q=python&format=json"

    # act
    response = requests.get(url)
    body = response.json()

    # assert
    assert response.status_code == 200
    assert 'Python' in body['AbstractURL']
