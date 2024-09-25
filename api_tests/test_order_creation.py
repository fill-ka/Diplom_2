import requests
from varaibles import *


def get_headers(auth_token=None):
    """Возвращает заголовки для запроса с авторизацией, если токен передан"""
    headers = {}
    if auth_token:
        headers = {"Authorization": f"Bearer {auth_token['accessToken']}"}
    return headers


def test_create_order_authorized(auth_token):
    url = f"{BASE_URL}/{ORDERS_END}"
    headers = get_headers(auth_token)

    response = requests.post(url, json=AUTHORIZED_ORDER_DATA, headers=headers)
    print("Status Code:", response.status_code)
    print("Response JSON:", response.json())
    assert response.status_code == 200


def test_create_order_unauthorized():
    url = f"{BASE_URL}/{ORDERS_END}"

    response = requests.post(url, json=UNAUTHORIZED_ORDER_DATA)
    assert response.status_code == 401  # Unauthorized


def test_create_order_invalid_ingredients(auth_token):
    url = f"{BASE_URL}/{ORDERS_END}"
    headers = get_headers(auth_token)

    response = requests.post(url, json=INVALID_INGREDIENTS_ORDER_DATA, headers=headers)
    assert response.status_code == 500
