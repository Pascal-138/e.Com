from starlette import status
from fastapi import Request, APIRouter
import re

# Обновленные регулярные выражения
validate_phone_number_pattern = r"^\+7 \d{3} \d{3} \d{2} \d{2}$"
validate_email_pattern = r"^[\w\.\-]+@[\w\-]+\.[a-zA-Z]{2,}$"
validate_date_patterns = [
    r"^\d{4}-\d{2}-\d{2}$",  # Формат: YYYY-MM-DD
    r"^\d{2}\.\d{2}\.\d{4}$"  # Формат: DD.MM.YYYY
]

router = APIRouter(prefix='')


def _get_form_data(data: dict):
    """Преобразование данных в зависимости от типа значения."""
    out = {}
    for key, value in data.items():
        if re.match(validate_phone_number_pattern, value):
            out[key] = "phone"
        elif re.match(validate_email_pattern, value):
            out[key] = "email"
        elif any(re.match(pattern, value) for pattern in validate_date_patterns):
            out[key] = "date"
        else:
            out[key] = "text"

    return out


@router.api_route(
    "/get_form",
    methods=["GET", "POST"],
    status_code=status.HTTP_200_OK,
    tags=["get_form"]
)
async def get_form(request: Request, data: dict = None):
    """Обработка запроса для получения типа данных."""
    if data is None:
        return {"error": "No data provided"}

    # Определение типов данных
    find_form_data = _get_form_data(data)

    # Получение ответа от службы (заглушка для примера)
    response = await request.app.template_service.get_form(find_form_data)
    return response
