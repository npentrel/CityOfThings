import os
from flask import Flask, jsonify
import urllib, json

app = Flask(__name__)


@app.route('/')
def Welcome():
    return app.send_static_file('index.html')


@app.route('/api/user', methods=['POST'])
def create_user():
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
            "id": count
            })    
        count += 1
    list2 = {"tasks": tasks}

    # list = { 
    #     "tasks":
    #         [
    #             {
    #                 "title": "Clean the road",
    #                 "content": "Lorem ipsum wololo ipsum",
    #                 "coordinates": [1.0, 2.0],
    #                 "address": "Rue de Wololo",
    #                 "category": "cleanup",
    #                 "time": "2012-04-23T18:25:43.511Z",
    #                 "id": 420
    #             }
    #         ]
    # }
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
