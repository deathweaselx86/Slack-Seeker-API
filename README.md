# Slack-Seeker-API

Easy shared search and annotations for the best slack messages.

This REPO serves as the API for the Slack seek.


## TODOs

- Walk up song
- Select presenters & plan presentation (Friday)
- add author and slack message content to SlackMessage model
- mrkdwn in messages?


## How do we update a saved message?

How to pick the message to update?
    - By unique ID? Already exists...
    - By UI?  e.g. click the message and you get into an event "chain"?
        - https://api.slack.com/bot-users#handling-events

- Add a tag
- Change description


# Team Members

- Mike Nguyen
- Jess McKinnie
- Jahnavi Bantupalli
- Brandon David
- Jerry Chen
- Trent Robbins


## How to install

1. Clone the repo using git clone <url>
2. Install virtualenv using command "sudo pip3 install virtualenv"
3. Create virtual environment venv_flask using "python3 -m venv venv_flask"
4. Activate virtual environment using source venv_flask/bin/activate
5. Install dependencies using pip3 install -r requirements.txt
6. Run command "export FLASK_ENV=development"
7. Run the flask app using "python3 run.py"



