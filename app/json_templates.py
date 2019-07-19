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
                    "text": "`/seeker search \"[text]\" [tag1] [tag2] [tag3]...`"
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
                    "text": "`/seeker save [message_URL] [tag1] [tag2] [tag3]... | [description]`"
                }
            },
            {
                "type": "context",
                "elements": [
                    {
                        "type": "mrkdwn",
                        "text": "Save a slack message URL with tags and a description. To get a slack message URL, press the message `...` icon."
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
                    "text": "`/seeker tag [message_id] [tag]`"
                }
            },
            {
                "type": "context",
                "elements": [
                    {
                        "type": "mrkdwn",
                        "text": "Add a tag to a message by message_id. Get the message id from `/seeker show` or `/seeker search`"
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
                    "text": "`/seeker untag [message_id] [tag]`"
                }
            },
            {
                "type": "context",
                "elements": [
                    {
                        "type": "mrkdwn",
                        "text": "Remove a tag from a message by message_id. Get the message id from `/seeker show` or `/seeker search`"
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

def seeker_show(tag, message_urls):
    return {
        "blocks": show_message_urls(tag, message_urls)
    }

def show_message_urls(tag, messages):
    message_blocks = [{
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "Here are the Slack messages with the tag `" + tag
        }
    }]
    for message in messages:
        tag_names=[]
        for tag in message.tags:
            tag_names.append(tag.name)
        message_blocks.append({
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "<" + message.url + "|link> *" + message.description + "* by " + message.author + ", id: " + str(
                    message.id) + " , tags: " + " ".join(tag_names) + "\n\t\t" + message.message_text
            }
            # "accessory": {
            #     "type": "button",
            #     "text": {
            #         "type": "plain_text",
            #         "text": ":+1:",
            #         "emoji": True
            #     },
            #     "value": "SOME_VALUE"
            # }
        })
    return message_blocks

# def url_string_or_slackmessage(url):
#     return url if isinstance(url, str) else url.url

def seeker_save(message_URL, tags, description):
    return {
        "blocks": [{
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "Alright! Saved *" + description + "*: " + message_URL + " with " + tags_plural(tags) + "`" +  "`, `".join(tags) + "`."
            }
        }]
    }

def seeker_search(terms, message_q):
    payload = {"blocks": [{
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "Here are the messages we found for \"" + (" ".join(terms)) + "\":"
        }
    }]}
    while not message_q.empty():
        message = message_q.get()

        payload["blocks"].append({
            "type": "context",
            "elements": [
                {
                    "type": "mrkdwn",
                    "text": "<" + message.url + "|link> *" + message.description + "* by " + message.author + ", id: " + str(message.id) + " , tags: " + " ".join(message.tags) + "\n\t\t" + message.message_text
                }
            ]
        })
    return payload

def seeker_unrecognized():
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
