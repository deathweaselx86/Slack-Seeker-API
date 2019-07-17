from flask import Flask
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy

from app.config import app_config
import json
import os
import flask
from flask import request
from urllib.parse import parse_qs
import sys
import parser

import json_templates


# app initiliazation
app = Flask(__name__)
env_name = os.getenv('FLASK_ENV')
app.config.from_object(app_config[env_name])
db = SQLAlchemy(app)

@app.route('/', methods=['GET'])
def get_all():
    return "hello world"

@app.route('/get_payload', methods=['GET', 'POST'])
def get_payload():

    payload = request.get_data()
    response = flask.make_response(payload, 200)
    return response

    return response

@app.route('/testjson', methods=['GET','POST'])
def get_json():

    payload = request.get_data(as_text=True)
    # payload = "token=nB2bAolyYp4uDT0hoqUyfVyv&team_id=T02V23TD2&team_domain=optimizely&channel_id=CLF247QJK&channel_name=hackweek2019-seeker&user_id=UGBCTP0AZ&user_name=trent.robbins&command=%2Fseeker-payload&text=&response_url=https%3A%2F%2Fhooks.slack.com%2Fcommands%2FT02V23TD2%2F690346166849%2FqeJF824OcWVD8tuLhmvwlYvt&trigger_id=696685010704.2988129444.7f616d9c52435a42645e726f26a42269"

    # resp wrapped in dict because it's sometimes an array
    # we should catch if there is no text in the command e.g. "/command <text>" where <text> is empty
    # because that is the case where it could just be a dict in a dict

    resp = {'key': parse_qs(payload)}
    #response = flask.make_response(jsonify(resp),200)

    parsed_payload = parser.parse(request.form['text'])

    # repeat for each command, we can fix the structure later

    # testing shim
    parsed_payload = {'command': 'help'}

    '''
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
    '''
    # if command not recognized
    else:
        # TODO: this probably fails due being dict(dict( instead of dict(list(dict -- handle this!
        response_payload = u'Invalid command: {}'.format(parsed_payload['command'])
    '''
    print(resp)
    if resp['key']['command'] == '/seeker':
        response_payload = u'Display seeker help if no parameter is provided... you provided the parameter {}'.format(parsed_payload['command'])
    else:
        # TODO: this probably fails due being dict(dict( instead of dict(list(dict -- handle this!
        response_payload = u'Invalid command: {}'.format(parsed_payload['command'])

    response = flask.make_response(response_payload, 200)

    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Content-Type'] = 'application/json'

    return response
