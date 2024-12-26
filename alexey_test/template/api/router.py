from fastapi import APIRouter
from template.api.ping import router as ping_router
from template.api.form import router as form_router

router = APIRouter()

# Подключение маршрутов
router.include_router(ping_router)
router.include_router(form_router)
