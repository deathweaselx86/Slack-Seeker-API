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
import app.text_parser as text_parser

import json_templates

#from app.helper import saveMessage
# from helper import saveMessage
from app import app, models, db, helper


@app.route('/', methods=['GET'])
def get_all():
    return "hello world"

@app.route('/get_payload', methods=['GET', 'POST'])
def get_payload():

    payload = request.get_data()
    response = flask.make_response(payload, 200)
    return response

@app.route('/testjson', methods=['GET','POST'])
def get_json():

    # payload = "token=nB2bAolyYp4uDT0hoqUyfVyv&team_id=T02V23TD2&team_domain=optimizely&channel_id=CLF247QJK&channel_name=hackweek2019-seeker&user_id=UGBCTP0AZ&user_name=trent.robbins&command=%2Fseeker-payload&text=&response_url=https%3A%2F%2Fhooks.slack.com%2Fcommands%2FT02V23TD2%2F690346166849%2FqeJF824OcWVD8tuLhmvwlYvt&trigger_id=696685010704.2988129444.7f616d9c52435a42645e726f26a42269"

    # resp wrapped in dict because it's sometimes an array
    # we should catch if there is no text in the command e.g. "/command <text>" where <text> is empty
    # because that is the case where it could just be a dict in a dict

    #response = flask.make_response(jsonify(resp),200)

    parsed_payload = text_parser.parse(request.form['text'])

    # repeat for each command, we can fix the structure later

    # testing shim
    # parsed_payload = {'command': 'help'}

    # repeat for each command, we can fix the structure later
    if parsed_payload['command'] == 'help' or parsed_payload['command'] == None:
        help_json_template = json_templates.seeker_help()
        response_payload = jsonify(help_json_template)

    # repeat for each command, we can fix the structure later
    elif parsed_payload['command'] == 'tags':
        tag_json_template = json_templates.seeker_tags()
        response_payload = jsonify(tag_json_template)

    elif parsed_payload['command'] == 'save':
        tokens = parsed_payload['payload']
        if len(tokens) != 3:
            return jsonify({"message":"Please give 3 parameters after save"})
        message_Url = tokens[0]
        description = tokens[1]
        tags = [tokens[2]]

        helper.saveMessage(message_Url, description,"", tags)
        response_payload = jsonify({"message":"Done saving the terms"})


    '''
    # if command not recognized
    else:
        # TODO: this probably fails due being dict(dict( instead of dict(list(dict -- handle this!
        response_payload = u'Invalid command: {}'.format(parsed_payload['command'])
    '''

    response = response_payload
    response.headers['Access-Control-Allow-Origin'] = '*'

    return response
