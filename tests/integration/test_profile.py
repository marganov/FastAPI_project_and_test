import allure

from tests.utils.client import login_user


@allure.epic("Аутентификация")
@allure.feature("Доступность профиля")
@allure.story("Позитивные кейсы")
@allure.title("Доступ к профилю с корректной cookie")
def test_profile_success(client):
    with allure.step("Логинимся"):
        login_resp, cookie = login_user("alexey", "password_alex", client)

    with allure.step("Запрашиваем профиль с cookie"):
        assert cookie is not None, "Cookie must not be None"
        profile_resp = client.get("/profile", cookies={"session_token": cookie})

    with allure.step("Проверяем статус и сообщение"):
        assert profile_resp.status_code == 200
        assert profile_resp.json()["message"] == "Welcome!"


@allure.epic("Аутентификация")
@allure.feature("Доступность профиля")
@allure.story("Негатвные кейсы")
@allure.title("Доступ к профилю без cookie")
def test_profile_fail_no_cookie(client):
    with allure.step("Запрашиваем профиль без cookie"):
        resp = client.get("/profile")

    with allure.step("Проверяем статус и сообщение"):
        assert resp.status_code == 401
        assert resp.json()["detail"] == "Unauthorized"


@allure.epic("Аутентификация")
@allure.feature("Доступность профиля")
@allure.story("Негатвные кейсы")
@allure.title("Доступ к профилю с некорректной cookie")
def test_profile_fail_invalid_cookie(client):
    with allure.step("Запрашиваем профиль с некорректной cookie"):
        resp = client.get("/profile", cookies={"session_token": "invalid_token"})

    with allure.step("Проверяем статус и сообщение"):
        assert resp.status_code == 401
        assert resp.json()["detail"] == "Unauthorized"
