import os


class Config:
    MONGO_URI = os.getenv("MONGO_URI")
    DBS_NAME = "recipesDB"
    USERS_COLLECTION = "users"
