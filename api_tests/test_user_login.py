import requests
from varaibles import *


def test_login_existing_user(auth_token):
    assert auth_token is not None


def test_login_invalid_credentials():
    url = f"{BASE_URL}/{AUTH_LOGIN_END}"
    user_data = {
        "email": "invalid_user@example.com",
        "password": "WrongPassword"
    }
    response = requests.post(url, json=user_data)
    assert response.status_code == 401  # Unauthorized
