from app import mongo

users_collection = mongo.db.users


def get_users():
    return users_collection.find()


def get_user(username):
    return users_collection.find_one({"username": username})
