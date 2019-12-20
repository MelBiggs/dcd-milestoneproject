import os
from flask import Flask, render_template, redirect, request, url_for


from os import path
if path.exists("env.py"):
    import env

app = Flask(__name__)

#MONGODB_NAME = os.environ.get('MONGODB_NAME')
app.config['MONGO_URI'] = os.environ.get('MONGO_URI')

@app.route('/')
def hello_world():
    return "Hello World"

# execute app__init__.py
if __name__ == "__main__":
    print(os.environ.get('MONGO_URI'))
    app.run(host='0.0.0.0', port=5000)
