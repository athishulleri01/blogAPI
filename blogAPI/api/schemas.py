import motor.motor_asyncio
from bson import ObjectId
import os


# load env
load_dotenv()
client = motor.motor_asyncio.AsyncIOMotorClient(os.getenv('MONGODB_URL'))


db = client.blog_api

# BSON and fastapoi JSON
class PyObjectId(ObjectId):
    @classmethod
    def  __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid")