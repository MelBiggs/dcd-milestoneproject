from flask import Flask
from flask_pymongo import PyMongo
from app.config import Config


mongo = PyMongo()


def create_app(config_class=Config):
    # app initialization + configuration
    app = Flask(__name__)
    app.config.from_object(config_class)

    # extensions for app init from above
    mongo.init_app(app)

    from app.users.routes import users
    app.register_blueprint(users)

    return app

# def mongo_connect(url):
#     try:
#         conn = pymongo.MongoClient(url)
#         print("Mongo is connected!")
#         return conn
#     except pymongo.errors.ConnectionFailure as error:
#         print("Could not connect to Mongo: %s") % error


# conn = mongo_connect(Config.MONGO_URI)
# coll = conn[Config.DBS_NAME][Config.USERS_COLLECTION]
# documents = coll.find()

# for doc in documents:
#     print(doc)
