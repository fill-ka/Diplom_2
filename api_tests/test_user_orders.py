import requests
import pytest
from varaibles import *

def test_get_user_orders_authorized():
    url = f"{BASE_URL}/orders"
    headers = {"Authorization": f"Bearer {AUTH_TOKEN_REFRESH}"}
    response = requests.get(url, headers=headers)
    assert response.status_code == 200


def test_get_user_orders_unauthorized():
    url = f"{BASE_URL}/orders"
    response = requests.get(url)
    assert response.status_code == 401  # Unauthorized
