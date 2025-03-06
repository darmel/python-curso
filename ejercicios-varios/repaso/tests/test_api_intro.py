# test api tests

import pytest
import requests
import warnings


@pytest.mark.api
@pytest.mark.duckduckgo
def test_duckduckgo_instant_answer_api():
    # Arrange
    url = "https://api.duckduckgo.com/?q=python+programming&format=json"

    # Act
    response = requests.get(url)  # garda la respuesta
    warnings.warn(UserWarning("{}".format(response)))
    # print("esto es la respuesta raw: ", response)
    body = response.json()  # trasnforma la respuesta en un diccionario
    warnings.warn(UserWarning("{}".format(body)))
    # print("esto es la respuesta parseada: ", body)

    # Assert
    assert response.status_code == 200
    assert 'Python' in body['AbstractText']
