import json
import requests
from jsonschema import validate

from utils.resource import path


def test_successful_registration(base_url):
    response = requests.post(
        base_url + '/api/register', data={"email": "eve.holt@reqres.in", "password": "pistol"}
    )
    body = response.json()
    schema = path('register.json')

    assert response.status_code == 200
    with open(schema) as file:
        f = file.read()
        validate(body, schema=json.loads(f))


def test_unsuccessful_registration(base_url):
    response = requests.post(
        base_url + '/api/register', data={"email": "sydney@fife"}
    )
    body = response.json()
    schema = path('bad_register.json')

    assert response.status_code == 400
    with open(schema) as file:
        f = file.read()
        validate(body, schema=json.loads(f))
