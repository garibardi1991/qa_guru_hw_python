import json
import requests
from jsonschema import validate

from utils.resource import path


def test_update_user(base_url):
    new_user_id = requests.post(
        base_url + '/api/users/', data={"name": "morpheus", "job": "zion resident"}
    ).json()['id']

    response = requests.put(
        url=f"{base_url}/api/users/{new_user_id}", data={"name": "morpheus", "job": "zion resident"}
    )
    body = response.json()
    schema = path('put_method.json')

    assert response.status_code == 200
    with open(schema) as file:
        f = file.read()
        validate(body, schema=json.loads(f))

