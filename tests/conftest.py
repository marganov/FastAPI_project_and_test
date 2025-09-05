import pytest
from fastapi.testclient import TestClient

from routers.routers import app


@pytest.fixture
def client():
    """Создает новый изолированный клиент для каждого теста"""
    return TestClient(app)
