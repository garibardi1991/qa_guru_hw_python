import json
import requests
from jsonschema import validate
from utils.resource import path


def test_return_single_user(base_url):
    response = requests.get(
        base_url + '/api/users/2'
    )
    body = response.json()
    schema = path('get_method.json')

    assert response.status_code == 200
    with open(schema) as file:
        f = file.read()
        validate(body, schema=json.loads(f))


def test_return_nonexistent_user(base_url):
    response = requests.get(
        base_url + '/api/users/1488'
    )

    assert response.status_code == 404
    assert response.json() == {}
