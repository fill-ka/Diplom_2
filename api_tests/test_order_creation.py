import requests
import pytest
from varaibles import *
import json


def test_create_order_authorized(auth_token):
    url = f"{BASE_URL}/{orders_end}"
    headers = {"Authorization": f"Bearer {auth_token['accessToken']}"}
    order_data = {
        "ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f"]
    }
    response = requests.post(url, json=order_data, headers=headers)
    print("Status Code:", response.status_code)
    print("Response JSON:", response.json())
    assert response.status_code == 200


def test_create_order_unauthorized():
    url = f"{BASE_URL}/{orders_end}"
    order_data = {
        "ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f"]
    }
    response = requests.post(url, json=order_data)
    assert response.status_code == 401  # Unauthorized


def test_create_order_invalid_ingredients(auth_token):
    url = f"{BASE_URL}/{orders_end}"
    headers = {"Authorization": f"Bearer {auth_token['accessToken']}"}
    order_data = {
        "ingredients": ["123"]
    }
    response = requests.post(url, json=order_data, headers=headers)
    assert response.status_code == 500
