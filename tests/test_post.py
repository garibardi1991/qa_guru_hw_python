import json
import requests
from jsonschema import validate

from utils.resource import path


def test_create_new_user(base_url):
    response = requests.post(
        base_url + '/api/users', data={"name": "morpheus", "job": "leader"}
    )
    body = response.json()
    schema = path('post_method.json')

    assert response.status_code == 201
    with open(schema) as file:
        f = file.read()
        validate(body, schema=json.loads(f))


