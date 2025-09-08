import pytest
from fastapi.testclient import TestClient

from main import app


@pytest.fixture
def client():
    """Создает новый изолированный клиент для каждого теста"""
    return TestClient(app)
