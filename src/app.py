from flask import Flask
from flask import jsonify
from src.config import app_config
import json
import os
import sys


def create_app(env_name):
    """
    Create app
    """

    # app initiliazation
    app = Flask(__name__)

    app.config.from_object(app_config[env_name])

    @app.route('/', methods=['GET'])
    def get_all():

        with open(os.path.join(sys.path[0], "src/data/list.json"), "r") as f:
            data =json.load(f)
        return jsonify(data)


    return app
