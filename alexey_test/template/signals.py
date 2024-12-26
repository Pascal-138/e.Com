# from .settings import Settings

# from motor import motor_asyncio

# from .service import TemplateService


# def setup_signals(app):

#     @app.on_event("startup")
#     async def on_startup():
#         app.config = Settings()
#         app.mongo = motor_asyncio.AsyncIOMotorClient(app.config.MONGO_URL)
#         app.template_service = TemplateService(app_config=app.config,
#                                                mongo=app.mongo)

#     @app.on_event("shutdown")
#     async def on_shutdown():
#         pass

from fastapi import FastAPI
from contextlib import asynccontextmanager


def setup_signals(app: FastAPI):
    @asynccontextmanager
    async def lifespan(app: FastAPI):
        # Выполнить действия при старте
        print("Startup logic")
        yield
        # Выполнить действия при завершении
        print("Shutdown logic")

    app.router.lifespan_context = lifespan
