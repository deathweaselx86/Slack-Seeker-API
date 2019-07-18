import queue as Q

def seeker_help():
    return {
        "blocks": [
            {
                "type": "section",
                "text": {
                    "type": "plain_text",
                    "text": "Looking for help? Try using these commands:"
                }
            },
            {
                "type": "divider"
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "`/seeker tags`"
                }
            },
            {
                "type": "context",
                "elements": [
                    {
                        "type": "mrkdwn",
                        "text": "Lists all tags created in our workspace."
                    }
                ]
            },
            {
                "type": "divider"
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "`/seeker show [tag]`"
                }
            },
            {
                "type": "context",
                "elements": [
                    {
                        "type": "mrkdwn",
                        "text": "List message URLs with the provided tag."
                    }
                ]
            },
            {
                "type": "divider"
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "`/seeker search \"[text]\" [tag 1] [tag 2] [tag 3]...`"
                }
            },
            {
                "type": "context",
                "elements": [
                    {
                        "type": "mrkdwn",
                        "text": "List message URLs with descriptions related to provided string. Can be filtered to specific tags."
                    }
                ]
            },
            {
                "type": "divider"
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "`/seeker save [message_URL] [tag1] [tag 2] [tag 3]... | [description]`"
                }
            },
            {
                "type": "context",
                "elements": [
                    {
                        "type": "mrkdwn",
                        "text": "Save a message to seeker."
                    }
                ]
            }
        ]
    }

def seeker_tags(tag_list):
    return {
        "blocks": [{
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "Here's a list of tags that you can query:\n\n" + list_tags(tag_list)
            }
        }]
    }

def list_tags(tag_list):
    return "\n".join(tag_list)

def seeker_tag(tag):
    return {
        "blocks": [{
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "Here are the Slack messages with the tag `" + tag + "`. Help your coworkers out and leave a thumbs up on the messages that were helpful!"
            }
        }]
    }

def seeker_save(message_URL, tags, description):
    return {
        "attachments": [{
            "blocks": [{
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Alright! Saved *" + description + "*: " + message_URL + " with " + tags_plural(tags) + ", ".join(tags) + "."
                }
            }]
        }]
    }

def seeker_search(message_q):
    payload = {"blocks": [{
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "Here are the messages we found:"
        }
    }]}
    while not message_q.empty():
        message = message_q.get()
        payload["blocks"].append({
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "<" + message.url + "|" + message.description + ">"
                }
            })
    return payload

def seeker_unrecognized(tag_list):
    return {
        "blocks": [{
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "Sorry, command not recognized"
            }
        }]
    }

def tags_plural(tags):
    return "tags " if len(tags) > 1 else "tag "

def seeker_save_msgURL():
    return '''[{"type": "section","text": {"type": "mrkdwn","text": "Time to save a message to Seeker! What's the Slack message URL?"}},]'''

def seeker_save_desc():
    return '''[{"type": "section","text": {"type": "mrkdwn","text": "Okay! please provide a short description (a sentence or less) of the message."}},]'''

def seeker_save_tag():
    return '''{"type": "section","text": {"type": "mrkdwn","text": "Great! Now assign a tag to this Slack message.If the tag hasn't been created yet, we'll create it for you."}},]'''
