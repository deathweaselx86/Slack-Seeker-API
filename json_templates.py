def seeker_help():
    return r'''[{"type": "section", "text": {"type": "mrkdwn","text": "Looking for help? Try using these commands:"}},{"type": "section","text": {"type": "mrkdwn","text": "`/seeker tags`: lists all tags created in our workspace\n `/seeker tag:<tag>`: list message URLs with the provided tag\n `/seeker search \"string\"`: list message URLs with descriptions related to provided string\n `/seeker search \"string\" tag:<tag>`: list message URLs with related descriptions within the provided tag\n `/seeker save`: begin a multi-step conversation to save a message to seeker\n `/seeker save <message_URL> \"<description>\" <tag>`: save a message to seeker with the provided attributes"}}]'''

def seeker_tags():
    return r'''[{"type": "section","text": {"type": "mrkdwn","text": "Here's a list of tags that you can query:"}},{"type": "section","text": {"type": "mrkdwn","text": "insert\n tags\n here"}}]'''

def seeker_tag(tag):
    return '''[{"type": "section","text": {"type": "mrkdwn","text": "Here are the Slack messages with the tag `{''' + tag + '''}`. Help your coworkers out and leave a thumbs up on the messages that were helpful!"}},]'''

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


# seeker_tag_tag = [    
#     {
#         "type": "section",
#         "text": {
#             "type": "mrkdwn",
#             "text": "Here are the Slack messages with the tag `monolith_setup`. Help your coworkers out and leave a thumbs up on the messages that were helpful!"
#         }
#     },
#     {
#         "type": "section",
#         "text": {
#             "type": "mrkdwn",
#             "text": "*Monolith bug with secrets:* https://optimizely.slack.com/archives/SDHIOGH"
#         },
#         "accessory": {
#             "type": "button",
#             "text": {
#                 "type": "plain_text",
#                 "text": ":+1:",
#                 "emoji": true
#             },
#             "value": "some_value"
#         }
#     },
#     {
#         "type": "section",
#         "text": {
#             "type": "mrkdwn",
#             "text": "*Dependencies for monolith:* https://optimizely.slack.com/archives/EEIRUG"
#         },
#         "accessory": {
#             "type": "button",
#             "text": {
#                 "type": "plain_text",
#                 "text": ":+1:",
#                 "emoji": true
#             },
#             "value": "click_me_123"
#         }
#     },
#     {
#         "type": "section",
#         "text": {
#             "type": "mrkdwn",
#             "text": "*Monolith thing:* https://optimizely.slack.com/archives/SDGVERIUBG"
#         },
#         "accessory": {
#             "type": "button",
#             "text": {
#                 "type": "plain_text",
#                 "text": ":+1:",
#                 "emoji": true
#             },
#             "value": "click_me_123"
#         }
#     }
# ]