from fastapi import APIRouter

from . import ping, form


router = APIRouter(prefix='/api')
router.include_router(ping.router)
router.include_router(form.router)
