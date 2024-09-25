import requests
import random
import string
from varaibles import *


def generate_random_email():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=8)) + "@example.com"


def test_create_unique_user():
    url = f"{BASE_URL}/{AUTH_REG_END}"

    response = requests.post(url, json=USER_UNIQUE_DATA)
    assert response.status_code == 200
    assert response.json().get("success") is True


def test_create_existing_user():
    url = f"{BASE_URL}/{AUTH_REG_END}"

    requests.post(url, json=EXISTING_USER_DATA)

    response = requests.post(url, json=EXISTING_USER_DATA)
    assert response.status_code == 403
    assert response.json().get("message") == USER_EXIST_ERROR


def test_create_user_missing_field():
    url = f"{BASE_URL}/{AUTH_REG_END}"

    response = requests.post(url, json=USER_MISSING_FIELD_DATA)
    assert response.status_code == 403
    assert response.json().get("message") == MISSING_FIELD_ERROR
