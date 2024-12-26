from app.main import app  # Импортируем в начале файла

from fastapi.testclient import TestClient
import pytest

client = TestClient(app)


# Мок-класс для template_service
class MockTemplateService:
    async def get_form(self, data):
        # Возвращает тестовые данные
        return {"processed_data": data}


# Связываем мок-объект с приложением
app.template_service = MockTemplateService()

# Инициализация тестового клиента
client = TestClient(app)


def test_ping():
    response = client.get("/api/ping")
    assert response.status_code == 200
    assert response.json() == {"success": True}


@pytest.mark.parametrize("input_data, expected_response", [
    (
        {"user_phone": "+7 123 456 78 90", "user_email": "test@example.com"},
        {"user_phone": "phone", "user_email": "email"}
    ),
    (
        {"date_of_birth": "2023-12-19", "comments": "Just a comment"},
        {"date_of_birth": "date", "comments": "text"}
    ),
    (
        {"unknown_field": "random_string", "email_field": "user@test.com"},
        {"unknown_field": "text", "email_field": "email"}
    ),
])
def test_get_form(input_data, expected_response):
    response = client.post("/api/get_form", json=input_data)
    assert response.status_code == 200

    # Проверяем данные внутри processed_data
    assert response.json()["processed_data"] == expected_response