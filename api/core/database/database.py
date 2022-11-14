from beanie import init_beanie
import motor.motor_asyncio

from config import Settings
from api.subscriptions.schemas import Subscription

global_settings = Settings()


async def init_db():
    client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017/crm")

    await init_beanie(database=client.db_name, document_models=[Subscription])
