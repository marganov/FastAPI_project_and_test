import allure


@allure.epic("Аутентификация")
@allure.feature("Логин")
@allure.story("Негативные кейсы")
@allure.title("Ожидаем отказ в авторизации")
def test_login_fail_wrong_password(client):
    with allure.step("Отправляем неверный пароль"):
        resp = client.post(
            "/login", json={"username": "alexey", "password": "wrong_pass"}
        )

    with allure.step("Проверяем статус ответа"):
        assert resp.status_code == 401

    with allure.step("Проверяем сообщение Unauthorized"):
        assert resp.json()["detail"] == "Unauthorized"
