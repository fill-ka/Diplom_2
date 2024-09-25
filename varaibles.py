from api_tests.test_user_creation import generate_random_email

BASE_URL = "https://stellarburgers.nomoreparties.site/api"
ORDERS_END = "orders"
AUTH_REG_END = "auth/register"
AUTH_USER_END = "auth/user"
AUTH_LOGIN_END = "auth/login"
AUTHORIZED_ORDER_DATA = {
    "ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f"]
}
UNAUTHORIZED_ORDER_DATA = {
    "ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f"]
}
INVALID_INGREDIENTS_ORDER_DATA = {
    "ingredients": ["123"]
}
USER_UNIQUE_DATA = {
        "email": generate_random_email(),
        "password": "Password123",
        "name": "Unique User"
    }
EXISTING_USER_DATA = {
        "email": "existing_user@example.com",
        "password": "Password123",
        "name": "Existing User"
    }
USER_MISSING_FIELD_DATA = {
        "email": generate_random_email(),
        "password": "Password123"
    }
USER_EXIST_ERROR = "User already exists"
MISSING_FIELD_ERROR = "Email, password and name are required fields"