import requests
import pytest
from varaibles import *
import json


def test_create_order_authorized(auth_token):
    url = f"{BASE_URL}/{orders_end}"
    headers = {"Authorization": f"Bearer {auth_token['accessToken']}"}
    order_data = {
        "ingredients": ["60d3b41abdacab0026a733c6", "609646e4dc916e00276b2870"]
    }
    response = requests.post(url, json=order_data, headers=headers)
    print("Status Code:", response.status_code)
    print("Response JSON:", response.json())
    assert response.status_code == 200


def test_create_order_unauthorized():
    url = f"{BASE_URL}/{orders_end}"
    order_data = {
        "ingredients": ["60d3b41abdacab0026a733c6", "609646e4dc916e00276b2870"]
    }
    response = requests.post(url, json=order_data)
    assert response.status_code == 401  # Unauthorized


def test_create_order_invalid_ingredients(auth_token):
    url = f"{BASE_URL}/{orders_end}"
    headers = {"Authorization": f"Bearer {auth_token['accessToken']}"}
    order_data = {
        "ingredients": ["invalid_ingredient_id"]
    }
    response = requests.post(url, json=order_data, headers=headers)
    assert response.status_code == 400  # Bad Request
