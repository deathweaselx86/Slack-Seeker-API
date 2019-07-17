from flask import Flask
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy

from app.config import app_config
from app.helper import saveMessage
import json
import os
import flask
from flask import request
from urllib.parse import parse_qs
# from helper import saveMessage
import sys
import app.text_parser as text_parser

import json_templates

import models
import views

# app initiliazation
app = Flask(__name__)
env_name = os.getenv('FLASK_ENV')
app.config.from_object(app_config[env_name])

db = SQLAlchemy(app)

