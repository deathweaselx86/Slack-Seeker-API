import queue as Q
from app.models import Tag, SlackMessage, messagetags
from app.models.message import Message
from app import app, db

from string import ascii_letters, digits


def searchMessage(terms):
    q = Q.PriorityQueue()
    messages = SlackMessage.query.all()
    terms = strip_terms(terms)

    '''
    Create a new Message object here to put in the queue
    because at the moment, it's easier to just create an object with the property
    `score`, rather than injecting score into SlackMessage model
    '''
    for message in messages:
        msg = Message(id=message.id,
                        url=message.url,
                        description=message.description,
                        message_text=message.message_text,
                        score=0,
                        tags=message.tags,
                        author=message.author,
                        annotator=message.annotator)
        text = msg.description.lower() + " " + msg.message_text.lower() + " " + msg.annotator.lower()
        tags = set()
        for tag in msg.tags:
            tags.add(tag)
        for term in terms:
            if term in text:
                msg.setScore(msg.getScore() + 1)
            for tag in tags:
                if term in tag or tag in term:
                    msg.setScore(msg.getScore() + 5)
        if msg.getScore() > 0:
            q.put(msg)
    app.logger.info(q)
    return q

def searchMessageByTags(terms, tags):
    q = Q.PriorityQueue()
    db_messages = SlackMessage.query.all()
    messages = []
    # Iterate through each message in the database
    for msg in db_messages:
        # Create a Message object
        message = Message(id=msg.id,
                        url=msg.url,
                        description=msg.description,
                        message_text=msg.message_text,                          
                        score=0,
                        tags=msg.tags,
                        author=msg.author,
                        annotator=msg.annotator)
        # Check if the Message object has any tag that's in the query tags
        for tag in message.tags:
            # If so add the message into the messages list
            if tag in tags:
                messages.append(message)
                break
    
    # Now iterate through the list of messages that have relevant tag
    # and score them based on the terms in its description
    for message in messages:
        text = message.description.lower() + " " + message.message_text.lower() + " " + message.annotator.lower()
        for term in terms:
            if term in text:
                message.setScore(message.getScore() + 1)
        if message.getScore() > 0:
            q.put(message)
    return q
    
def saveMessage(url, description, message_text, annotator, tags, author="None"):
    db_tags = []
    for tag in tags:
        tag_obj = Tag.query.filter_by(name=tag).first()
        if tag_obj:
            db_tags.append(tag_obj)
        else:
            new_tag = Tag(name=tag)
            db_tags.append(new_tag)
            db.session.add(new_tag)
    new_message = SlackMessage(url=url,
                               description=description,
                               message_text=message_text,
                               author=author,
                               annotator=annotator)
    new_message.tags.extend(db_tags)
    db.session.add(new_message)
    db.session.commit()

def deleteMessage(url):
    message = SlackMessage.query.filter_by(url=url).first()
    if message is None: 
        return False
    else:
        db.session.delete(message)
        db.session.commit()
        return True

def updateMessage(url, **args):
    message = SlackMessage.query.filter_by(url=url).first()
    description = args.get('description', None)
    if not description is None:
        message.description = description
    message_text = args.get('text', None)
    if not message_text is None:
        message.message_text = message_text
    tags = args.get('tags', None)
    if not tags is None:
        tag_name = set()
        for msg_tag in message.tags:
            tag_name.add(msg_tag.name)
        for tag in tags:
            if not tag in tag_name:
                new_tag = Tag(name=tag)
                db.session.add(new_tag)
                message.tags.append(new_tag)
    author = args.get('author', None)
    if not author is None:
        message.author = author
    annotator = args.get('annotator', None)
    if not annotator is None:
        message.annotator = annotator
    db.session.commit()


def strip_terms(terms):
    ''' convert each term in terms to just letters and numbers

    terms - list of strings
    '''
    allowed_glyphs = ascii_letters + digits + "'" 

    stripped_terms = []
    for term in terms:
        stripped_term = ''
        for letter in term:
            if letter in allowed_glyphs:
                stripped_term += letter
            else:
                stripped_terms.append(stripped_term)
                stripped_term = ''
        if stripped_term:
            stripped_terms.append(stripped_term)

    return stripped_terms

def get_all_messages_by_tag(tag):
    messages_by_tag =[]
    messages_by_tag =  SlackMessage.query.join(messagetags).join(Tag).filter(Tag.name == tag).all()


    return messages_by_tag

def get_all_messages():
    messages = SlackMessage.query.all()
    return messages
