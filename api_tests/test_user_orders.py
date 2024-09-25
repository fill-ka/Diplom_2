import requests
from varaibles import *


def test_get_user_orders_authorized(auth_token):
    url = f"{BASE_URL}/{ORDERS_END}"
    headers = {"Authorization": f"Bearer {auth_token['accessToken']}"}
    response = requests.get(url, headers=headers)
    assert response.status_code == 200


def test_get_user_orders_unauthorized():
    url = f"{BASE_URL}/{ORDERS_END}"
    response = requests.get(url)
    assert response.status_code == 401  # Unauthorized
