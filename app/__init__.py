from flask import Flask
from flask import jsonify
from app.config import app_config
import json
import os
import sys


# app initiliazation
app = Flask(__name__)
env_name = os.getenv('FLASK_ENV')
app.config.from_object(app_config[env_name])


@app.route('/', methods=['GET'])
def get_all():
    return "hello world"


