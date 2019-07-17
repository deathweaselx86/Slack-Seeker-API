from flask_sqlalchemy import SQLAlchemy
from app import app

db = SQLAlchemy(app)

messagetags = db.Table('messagetags',
    db.Column('tag_id', db.Integer, db.ForeignKey('tags.id'), primary_key=True, nullable=False),
    db.Column('message_id', db.Integer, db.ForeignKey('slackmessages.id'), primary_key=True, nullable=False))

class Tag(db.Model):
    __tablename__='tags'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)


class SlackMessage(db.Model):
    __tablename__='slackmessages'
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(512), unique=True, nullable=False)
    description = db.Column(db.String(512), nullable=False)
    message_text = db.Column(db.String(1000), unique=True, nullable=False)
    tags = db.relationship('Tag', secondary=messagetags, backref=db.backref('slackmessages'))
