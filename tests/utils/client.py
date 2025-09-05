from fastapi.testclient import TestClient

from routers.routers import app

client = TestClient(app)


def login_user(username: str, password: str, test_client=None):
    if test_client is None:
        test_client = client
    resp = test_client.post("/login", json={"username": username, "password": password})
    cookie = resp.cookies.get("session_token")
    return resp, cookie
