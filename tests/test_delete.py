import requests


def test_delete_user(base_url):
    new_user_id = requests.post(
        base_url + '/api/users/', data={"name": "John", "job": "officer"}
    ).json()['id']

    response = requests.delete(url=f"{base_url}/api/users/{new_user_id}")

    assert response.status_code == 204
