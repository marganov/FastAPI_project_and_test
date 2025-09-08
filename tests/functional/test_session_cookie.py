import allure
import pytest

from security.config import settings
from security.cookies import COOKIE_NAME
from tests.utils.client import client, login_user


@allure.epic("Авторизация")
@allure.feature("Cookie-based сессии")
@pytest.mark.parametrize("max_age", [None, 3600])
def test_cookie_behavior(monkeypatch, max_age):
    """
    Проверяем корректность установки session cookie
    при разных значениях SESSION_MAX_AGE
    """

    with allure.step(f"Патчим settings.SESSION_MAX_AGE = {max_age}"):
        monkeypatch.setattr(settings, "SESSION_MAX_AGE", max_age)

    with allure.step("Отправляем запрос /login для авторизации"):
        response, session_cookie = login_user("alexey", "password_alex")
        assert response.status_code == 200, "Авторизация должна пройти успешно"

    with allure.step("Извлекаем cookie из ответа"):
        set_cookie_header = response.headers.get("set-cookie")
        allure.attach(
            set_cookie_header,
            name="Set-Cookie Header",
            attachment_type=allure.attachment_type.TEXT,
        )

        assert COOKIE_NAME in set_cookie_header, "Cookie сессии должен присутствовать"

    if max_age is None:
        with allure.step(
            "Проверяем, что cookie является сессионным (Max-Age отсутствует)"
        ):
            assert (
                "Max-Age" not in set_cookie_header
            ), "Сессионный cookie не должен иметь Max-Age"
    else:
        with allure.step(
            f"Проверяем, что cookie имеет ограничение жизни Max-Age={max_age}"
        ):
            assert (
                f"Max-Age={max_age}" in set_cookie_header
            ), f"Cookie должен содержать Max-Age={max_age}"

    with allure.step("Отправляем запрос /profile с полученными cookie"):
        profile_response = client.get("/profile", cookies={COOKIE_NAME: session_cookie})
        assert profile_response.status_code == 200, "Профиль должен быть доступен"

        allure.attach(
            str(profile_response.json()),
            name="Profile Response",
            attachment_type=allure.attachment_type.JSON,
        )
