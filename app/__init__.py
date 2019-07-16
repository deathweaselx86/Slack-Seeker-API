from flask import Flask
from flask import jsonify
from app.config import app_config
import json
import os
import flask
from flask import request
from urllib.parse import parse_qs
import sys


# app initiliazation
app = Flask(__name__)
env_name = os.getenv('FLASK_ENV')
app.config.from_object(app_config[env_name])


@app.route('/', methods=['GET'])
def get_all():
    return "hello world"


@app.route('/testjson', methods=['GET','POST'])
def get_json():

    dirname = os.path.dirname(__file__)
    payload = request.get_data()
    resp = {'key':parse_qs(payload, encoding='utf-8')}
    print(jsonify(resp['key']))
    response = flask.make_response(jsonify(resp),200)
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Content-Type'] = 'application/json'

    return response