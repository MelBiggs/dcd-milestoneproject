import os
from app import create_app
from app.config import Config


app = create_app(Config)

# execute app__init__.py
if __name__ == "__main__":
    app.run(host=os.getenv("IP"), port=os.getenv("PORT"))
