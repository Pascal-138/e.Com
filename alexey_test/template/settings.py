import os
from motor.motor_asyncio import AsyncIOMotorClient


class Settings:
    # APP section
    HOST: str = "127.0.0.1"
    PORT: int = 8000

    # MONGO SETTINGS section
    MONGO_HOST: str = os.getenv("MONGO_HOST", "localhost")
    MONGO_PORT: str = os.getenv("MONGO_PORT", "27017")
    MONGO_USER: str = os.getenv("MONGO_USER", "verified_user")
    MONGO_PASSWORD: str = os.getenv("MONGO_PASSWORD", "very_secret_password")
    MONGO_NAME: str = os.getenv("MONGO_NAME", "templates")
    MONGO_COLLECTION_FORMS: str = os.getenv("MONGO_COLLECTION_FORMS", "forms")

    # Формирование корректного Mongo URL
    MONGO_URL: str = (
        f"mongodb://{os.getenv('MONGO_USER', 'verified_user')}:"
        f"{os.getenv('MONGO_PASSWORD', 'very_secret_password')}@"
        f"{os.getenv('MONGO_HOST', 'localhost')}:"
        f"{os.getenv('MONGO_PORT', '27017')}/"
        f"{os.getenv('MONGO_NAME', 'templates')}"
    )

    def __init__(self):
        # Инициализация клиента MongoDB
        self.client = AsyncIOMotorClient(self.MONGO_URL)
        self.db = self.client[self.MONGO_NAME]
        self.forms_collection = self.db[self.MONGO_COLLECTION_FORMS]

    async def initialize_db(self):
        """Заполняет коллекцию форм, если она пуста."""
        if await self.forms_collection.count_documents({}) == 0:
            initial_data = [
                {"name": "User Registration", "fields": {"user_email": "email", "user_phone": "phone"}},
                {"name": "Order Form", "fields": {"order_date": "date", "customer_email": "email"}}
            ]
            await self.forms_collection.insert_many(initial_data)


settings = Settings()
