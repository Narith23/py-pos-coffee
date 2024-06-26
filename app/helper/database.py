from app.helper.config import MONGO_DATABASE, MONGO_DETAILS
from motor.motor_asyncio import AsyncIOMotorClient

client = AsyncIOMotorClient(MONGO_DETAILS)

# database
database = client.get_database(MONGO_DATABASE)

# collections
users = database.get_collection("users")
categories = database.get_collection("categories")
products = database.get_collection("products")