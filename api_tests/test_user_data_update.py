import requests
import pytest
from varaibles import *


def test_update_user_data_authorized(auth_token):
    url = f"{BASE_URL}/{auth_user_end}"
    headers = {"Authorization": f"Bearer {auth_token['accessToken']}"}
    user_data = {
        "name": "Updated Name"
    }
    response = requests.patch(url, json=user_data, headers=headers)
    assert response.status_code == 200
    assert response.json().get("name") == "Updated Name"


def test_update_user_data_unauthorized():
    url = f"{BASE_URL}/{auth_user_end}"
    user_data = {
        "name": "Updated Name"
    }
    response = requests.patch(url, json=user_data)
    assert response.status_code == 401  # Unauthorized
