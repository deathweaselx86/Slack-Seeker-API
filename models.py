# this is not going to work as is
from flask_sqlalchemy import SQLAlchemy
from app import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/temp.db'
db = SQLAlchemy(app)


messagetags = db.Table('messagetags',
                       db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True),
                       db.Column('message_id', db.Integer, db.ForeignKey('slackmessage.id'), primary_key=True))


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)


class SlackMessage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # probably too many characters, but better safe than sorry
    url = db.Column(db.String(512), unique=True, nullable=False)
    description = db.Column(db.String(512), nullable=False)
