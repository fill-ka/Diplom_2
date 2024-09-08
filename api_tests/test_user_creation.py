import requests
import pytest
from varaibles import BASE_URL



def test_create_unique_user():
    url = f"{BASE_URL}/auth/register"
    user_data = {
        "email": "unique_user@example.com",
        "password": "Password123",
        "name": "Unique User"
    }
    response = requests.post(url, json=user_data)
    assert response.status_code == 200
    assert response.json().get("success") is True


def test_create_existing_user():
    url = f"{BASE_URL}/auth/register"
    user_data = {
        "email": "existing_user@example.com",
        "password": "Password123",
        "name": "Existing User"
    }
    # First create the user
    requests.post(url, json=user_data)
    # Try creating the user again
    response = requests.post(url, json=user_data)
    assert response.status_code == 403  # Assuming 403 for user already exists


def test_create_user_missing_field():
    url = f"{BASE_URL}/auth/register"
    user_data = {
        "email": "missing_field_user@example.com",
        "password": "Password123"
        # Missing 'name'
    }
    response = requests.post(url, json=user_data)
    assert response.status_code == 400  # Bad Request
