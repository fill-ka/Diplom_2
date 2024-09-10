import pytest
import requests
from varaibles import *

@pytest.fixture(scope="module")
def auth_token():
    url = f"{BASE_URL}/{auth_login_end}"
    user_data = {
        "email": "anna_komova_7_251@gmail.com",
        "password": "Q1w2e3r4t5"
    }

    response = requests.post(url, json=user_data)

    if response.status_code != 200:
        pytest.fail(f"Failed to log in: {response.status_code} - {response.text}")

    response_data = response.json()
    access_token = response_data.get("accessToken")
    refresh_token = response_data.get("refreshToken")

    if access_token is None:
        pytest.fail("Access token not received in response")
    if refresh_token is None:
        pytest.fail("Refresh token not received in response")

    yield {
        "accessToken": access_token.replace("Bearer ", ""),  # Удалите Bearer
        "refreshToken": refresh_token
    }
