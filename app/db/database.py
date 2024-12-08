from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from app.core.config import settings
from app.models.form_template import FormTemplate


async def init_db():
    try:
        client = AsyncIOMotorClient(settings.MONGODB_URL)
        await init_beanie(
            database=client[settings.DATABASE_NAME], document_models=[FormTemplate]
        )
    except Exception as e:
        print(f"Database initialization failed: {e}")
        raise e
