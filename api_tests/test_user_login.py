import requests
import pytest
from varaibles import BASE_URL


def test_login_existing_user():
    url = f"{BASE_URL}/auth/login"
    user_data = {
        "email": "existing_user@example.com",
        "password": "Password123"
    }
    response = requests.post(url, json=user_data)
    assert response.status_code == 200
    assert response.json().get("success") is True


def test_login_invalid_credentials():
    url = f"{BASE_URL}/auth/login"
    user_data = {
        "email": "invalid_user@example.com",
        "password": "WrongPassword"
    }
    response = requests.post(url, json=user_data)
    assert response.status_code == 401  # Unauthorized
