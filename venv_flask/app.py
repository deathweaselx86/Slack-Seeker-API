from flask import Flask
from config import app_config


def create_app(env_name):
    """
    Create app
    """

    # app initiliazation
    app = Flask(__name__)

    app.config.from_object(app_config['development'])

    @app.route('/', methods=['GET'])
    def get_all():
        return "hello"


    return app
