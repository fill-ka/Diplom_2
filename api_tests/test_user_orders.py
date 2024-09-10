import requests
import pytest
from varaibles import *


def test_get_user_orders_authorized(auth_token):
    url = f"{BASE_URL}/{orders_end}"
    headers = {"Authorization": f"Bearer {auth_token}"}
    response = requests.get(url, headers=headers)
    assert response.status_code == 200


def test_get_user_orders_unauthorized():
    url = f"{BASE_URL}/{orders_end}"
    response = requests.get(url)
    assert response.status_code == 401  # Unauthorized
