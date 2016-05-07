import os
from flask import Flask, jsonify, request
import urllib
import json
import random

import requests

from data import new_customer

app = Flask(__name__)

auth_token = 'MjI4ODhjMDg4NjBkODZiNjEyYWI4ZjI4NmZjNzMxMjgxNzc2MTlmOTUzN2VjOTJjOWM6bHMxREdra3k0dG9sWmFqdWJzcjJ5NUV0YTZsanZBbDFYRXVqejB5MkpxZTFWUnBLY0E='

@app.route('/')
def Welcome():
    return app.send_static_file('index.html')


@app.route('/api/user', methods=['POST'])
def create_user():
    new_customer['name'] = "{} {}".format(request.args.get('FirstName'),
                                      request.args.get('LastName'))
    new_customer['contactMedium']['medium']['emailAddress'] = request.args.get('Email')

    # requests.post

    response = {
        "userid": 31337
    }
    return jsonify(response)


@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    url = "http://www.amsterdamopendata.nl/files/Festivals.json"
    response = urllib.urlopen(url)
    data = json.loads(response.read())
    count = 0
    tasks = []
    for d in data:
        tasks.append({
            "title": d['title'],
            "content": d['details']['en']['shortdescription'],
            "coordinates": [d['location']['latitude'], d['location']['longitude']],
            "address": d['location']['adress'],
            "category": "cleanup",
            "time": d['details']['en']['calendarsummary'],
            "id": count,
            "reward": random.uniform(4.0, 7.5)
            })
        count += 1
    list2 = {"tasks": tasks}

    return jsonify(list2)


@app.route('/api/tasks/signup')
def signup_task():
    return jsonify('OK')


@app.route('/api/rewards', methods=['GET'])
def get_rewards():
    rewards = {"rewards": [
        {
            "title": "Amazon $100 voucher",
            "content": "Amazing Content",
            "points": 100,
            "id": 1337,
        }
    ]}
    return jsonify(rewards)


@app.route('/api/rewards/<int:reward_id>', methods=['GET'])
def RedeemReward(reward_id):
    response = {
        "error": "insuficientFunds"
    }
    return jsonify(response)


port = os.getenv('PORT', '5000')
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(port), debug=True)
