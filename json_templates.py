def seeker_help():
    return {
        "attachments": [{
            "blocks": [{
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Here's a list of tags that you can query:"
                }
            }]
        }]
    }

def seeker_tags(tag_list):
    return {
        "attachments": [{
            "blocks": [{
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Here's a list of tags that you can query:"
                }
            },{
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": list_tags(tag_list)
                }
            }]
        }]
    }
    # return '''[{"type": "section","text": {"type": "mrkdwn","text": "Here's a list of tags that you can query:"}},{"type": "section","text": {"type": "mrkdwn","text": "''' + list_tags(tag_list) + '''"}}]'''

def list_tags(tag_list):
    return "\n".join(tag_list)

def seeker_tag(tag):
    return '''[{"type": "section","text": {"type": "mrkdwn","text": "Here are the Slack messages with the tag `{''' + tag + '''}`. Help your coworkers out and leave a thumbs up on the messages that were helpful!"}},]'''

def seeker_save(message_URL, description, tag):
    return '''[{"type": "section","text": {"type": "mrkdwn","text": "Alright! Saved "*''' + description + ''':* ''' + message_URL + ''' with tag `''' + tag + '''`.}},]'''

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
