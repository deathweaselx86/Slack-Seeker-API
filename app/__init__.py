from flask import Flask
from flask import jsonify
from app.config import app_config
import json
import os
import flask
from flask import request
from urllib.parse import parse_qs
import sys

import json_templates


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

    # resp wrapped in dict because it's sometimes an array
    # we should catch if there is no text in the command e.g. "/command <text>" where <text> is empty
    # because that is the case where it could just be a dict in a dict

    resp = {'key':parse_qs(payload, encoding='utf-8')}
    #response = flask.make_response(jsonify(resp),200)

    # repeat for each command, we can fix the structure later
    if payload['command'] == '/seeker':

        response_payload = u'Display seeker help if no parameter is provided...'

    '''
    # testing shim
    parsed_payload = {'command': 'help'}

    # repeat for each command, we can fix the structure later
    if parsed_payload['command'] == 'tags':
        tag_json_template = json_template.seeker_tags()
        tag_list = ['tag1', 'tag2', 'tag3']
        response_payload = jsonify(tag_json_template)

    # repeat for each command, we can fix the structure later
    if parsed_payload['command'] == 'help':
        help_json_template = json_template.seeker_help()
        response_payload = jsonify(taglist)
    '''


    # if command not recognized
    else:
        response_payload = u'Invalid command: {}'.format(parsed_payload['command'])

    response = flask.make_response(payload, 200)

    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Content-Type'] = 'application/json'

    return response
