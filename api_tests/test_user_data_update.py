import requests
import pytest
from varaibles import *


def test_update_user_data_authorized(auth_token):
    url = f"{BASE_URL}/{auth_user_end}"
    headers = {"Authorization": f"Bearer {auth_token['accessToken']}"}

    # Данные для обновления пользователя
    user_data = {
        "email": "anna_komova_7_251@gmail.com",
        "name": "Olga"
    }

    # Отправляем PATCH запрос для обновления данных пользователя
    patch_response = requests.patch(url, json=user_data, headers=headers)

    assert patch_response.status_code == 200
    assert patch_response.json().get("user").get("name") == "Olga"

    # Отправляем GET запрос для получения обновленных данных
    get_response = requests.get(url, headers=headers)

    assert get_response.status_code == 200
    assert get_response.json().get("user").get("name") == "Olga"
    assert get_response.json().get("user").get("email") == "anna_komova_7_251@gmail.com"

    # Логирование для проверки
    print("PATCH Response JSON:", patch_response.json())
    print("GET Response JSON:", get_response.json())


def test_update_user_data_unauthorized():
    url = f"{BASE_URL}/{auth_user_end}"
    user_data = {
        "name": "Updated Name"
    }
    response = requests.patch(url, json=user_data)
    assert response.status_code == 401  # Unauthorized
