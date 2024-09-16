 # AsyncIOMotorClient is a class provided by the metro library.which is an asynchronous driver for MongoDB in Python.
from motor.motor_asyncio import AsyncIOMotorClient 

#PyMongoError is a base exception class provided by the pymongo library, which is used to handle exceptions related to MongoDB operations.
from pymongo.errors import PyMongoError
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URL = os.getenv("MONGO_URL")
client = AsyncIOMotorClient(MONGO_URL)
db = client['FastAPI']  

async def get_user_collection():
    try:
        return db['users']  
    except PyMongoError as e:
        print(f"Error connecting to MongoDB: {e}")