import allure

from tests.utils.client import login_user


@allure.epic("Аутентификация")
@allure.feature("Логин")
@allure.story("Позитивные кейсы")
@allure.title("Успешный логин, установка cookie, получение ID пользователя")
def test_login_success(client):
    with allure.step("Отправляем корректные логин/пароль"):
        resp, cookie = login_user("alexey", "password_alex", client)

    with allure.step("Проверяем статус ответа"):
        assert resp.status_code == 200

    with allure.step("Проверяем наличие user_id в ответе"):
        assert "user_id" in resp.json()

    with allure.step("Проверяем установку cookie session_token"):
        assert cookie is not None
