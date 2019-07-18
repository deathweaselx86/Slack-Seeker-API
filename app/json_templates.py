def seeker_help():
    return {
        "attachments": [{
            "blocks": [
                {
                    "type": "section",
                    "text": {
                        "type": "plain_text",
                        "text": "Looking for help? Try using these commands:",
                        "emoji": true
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
                        "text": "`/seeker tag [tag]`"
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
                        "text": "`/seeker search \"[text]\" (tag 1) (tag 2) (tag 3)...`"
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
                        "text": "`/seeker save [message_URL] \"[description]\" (tag1) (tag 2) (tag 3)...`"
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
        }]
    }

    # `/seeker save`: begin a multi-step conversation to save a message to seeker\n
    # `/seeker search \"string\" tag:<tag>`: list message URLs with related descriptions within the provided tag\n

def seeker_tags(tag_list):
    return {
        "attachments": [{
            "blocks": [{
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Here's a list of tags that you can query:\n\n" + list_tags(tag_list)
                }
            }]
        }]
    }
    # return '''[{"type": "section","text": {"type": "mrkdwn","text": "Here's a list of tags that you can query:"}},{"type": "section","text": {"type": "mrkdwn","text": "''' + list_tags(tag_list) + '''"}}]'''

def list_tags(tag_list):
    return "\n".join(tag_list)

def seeker_tag(tag):
    return {
        "attachments": [{
            "blocks": [{
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Here are the Slack messages with the tag `" + tag + "`. Help your coworkers out and leave a thumbs up on the messages that were helpful!"
                }
            }]
        }]
    }
    # return '''[{"type": "section","text": {"type": "mrkdwn","text": "Here are the Slack messages with the tag `{''' + tag + '''}`. Help your coworkers out and leave a thumbs up on the messages that were helpful!"}},]'''

def seeker_save(message_URL, description, tag):
    return {
        "attachments": [{
            "blocks": [{
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Alright! Saved *" + description + "*: " + message_URL + " with tags " + ", ".join(tag) + "."
                }
            }]
        }]
    }
    
    # return '''[{"type": "section","text": {"type": "mrkdwn","text": "Alright! Saved "*''' + description + ''':* ''' + message_URL + ''' with tag `''' + tag + '''`.}},]'''

def seeker_save_msgURL():
    return '''[{"type": "section","text": {"type": "mrkdwn","text": "Time to save a message to Seeker! What's the Slack message URL?"}},]'''

def seeker_save_desc():
    return '''[{"type": "section","text": {"type": "mrkdwn","text": "Okay! please provide a short description (a sentence or less) of the message."}},]'''

def seeker_save_tag():
    return '''{"type": "section","text": {"type": "mrkdwn","text": "Great! Now assign a tag to this Slack message.If the tag hasn't been created yet, we'll create it for you."}},]'''

### Example for how a Slack message's information should be displayed
# {
#     "type": "section",
#     "text": {
#         "type": "mrkdwn",
#         "text": "*Monolith bug with secrets:* https://optimizely.slack.com/archives/SDHIOGH"
#     },
#     "accessory": {
#         "type": "button",
#         "text": {
#             "type": "plain_text",
#             "text": ":+1:",
#             "emoji": true
#         },
#         "value": "some_value"
#     }
# }
