import requests
import pytest
import random
import string
from varaibles import *


def generate_random_email():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=8)) + "@example.com"


def test_create_unique_user():
    url = f"{BASE_URL}/{auth_reg_end}"
    user_data = {
        "email": generate_random_email(),
        "password": "Password123",
        "name": "Unique User"
    }
    response = requests.post(url, json=user_data)
    assert response.status_code == 200
    assert response.json().get("success") is True


def test_create_existing_user():
    url = f"{BASE_URL}/{auth_reg_end}"
    user_data = {
        "email": "existing_user@example.com",
        "password": "Password123",
        "name": "Existing User"
    }

    requests.post(url, json=user_data)

    response = requests.post(url, json=user_data)
    assert response.status_code == 403
    assert response.json().get("message") == "User already exists"


def test_create_user_missing_field():
    url = f"{BASE_URL}/{auth_reg_end}"
    user_data = {
        "email": generate_random_email(),
        "password": "Password123"
    }
    response = requests.post(url, json=user_data)
    assert response.status_code == 403
    assert response.json().get("message") == "Email, password and name are required fields"
