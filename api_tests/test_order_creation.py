import requests
import pytest
from varaibles import *


def test_create_order_authorized():
    url = f"{BASE_URL}/orders"
    headers = {"Authorization": f"Bearer {AUTH_TOKEN_REFRESH}"}
    order_data = {
        "ingredients": ["ingredient_id_1", "ingredient_id_2"]
    }
    response = requests.post(url, json=order_data, headers=headers)
    assert response.status_code == 200


def test_create_order_unauthorized():
    url = f"{BASE_URL}/orders"
    order_data = {
        "ingredients": ["ingredient_id_1"]
    }
    response = requests.post(url, json=order_data)
    assert response.status_code == 401  # Unauthorized


def test_create_order_invalid_ingredients():
    url = f"{BASE_URL}/orders"
    headers = {"Authorization": f"Bearer {AUTH_TOKEN}"}
    order_data = {
        "ingredients": ["invalid_ingredient_id"]
    }
    response = requests.post(url, json=order_data, headers=headers)
    assert response.status_code == 400  # Bad Request
