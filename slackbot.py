#!/usr/bin/env python

from flask import Flask, jsonify, request
import os
import dotenv
import spinitron_fetch


dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
dotenv.load_dotenv(dotenv_path)
verification_token = os.environ['VERIFICATION_TOKEN']

app = Flask(__name__)

@app.route('/spin', methods=['POST'])
def spin():
    if request.form['token'] == verification_token:
        payload = {"response_type": "in_channel",'text': spinitron_fetch.format_final_response()}
        return jsonify(payload)

@app.route('/')
def index():
    return "<a href=https://slack.com/oauth/v2/authorize?scope=app_mentions:read,channels:read,chat:write,chat:write.customize,reactions:write,commands&client_id=2665247242390.4335435150835&>Add to Slack</a>"



if __name__ == '__main__':
    app.run()