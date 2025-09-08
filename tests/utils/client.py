import allure
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def login_user(
    username: str = "testuser",
    password: str = "password123",
    test_client: TestClient | None = None,
):
    """
    Упрощённый хелпер для логина в тестах.
    Если аргументы не переданы — используем дефолтного тестового юзера.
    """
    client_to_use = test_client or client

    with allure.step(f"Авторизация пользователя {username}"):
        response = client_to_use.post(
            "/login",
            json={"username": username, "password": password},
        )

        session_cookie = response.cookies.get("session_token")

        allure.attach(
            str(response.json()),
            name="Login Response",
            attachment_type=allure.attachment_type.JSON,
        )

        return response, session_cookie
