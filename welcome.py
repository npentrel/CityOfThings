# Copyright 2015 IBM Corp. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def Welcome():
    return app.send_static_file('index.html')

@app.route('/myapp')
def WelcomeToMyapp():
    return 'Welcome again to my app running on Bluemix!'

@app.route('/api/people')
def GetPeople():
    list = [
        {'name': 'John', 'age': 28},
        {'name': 'Bill', 'val': 26}
    ]
    return jsonify(results=list)

@app.route('/api/people/<name>')
def SayHello(name):
    message = {
        'message': 'Hello ' + name
    }
    return jsonify(results=message)

@app.route('/api/user')
def CreateUser(name):
    response = {
        "userid": 31337
    }
    return jsonify(response)

@app.route('/api/rewards')
def GetRewards(task):
    rewards = {"Rewards": 
            [
                {
                    "title": "Amazon $100 voucher"
                    "content":
                    "points": 100
                    "id" : 1337
                },
            ]}
    return jsonify(rewards)

@app.route('/api/rewards/<id>')
def RedeemReward(id):
    response = {
        "error": "insuficientFunds"
    }
    return jsonify(response)

@app.route('/api/tasks')
def GetTasks():
    list = { 
        "tasks":
            [
                {
                    "title": "Clean the road"
                    "content": "Lorem ipsum wololo ipsum"
                    "coordinates": [1.0, 2.0]
                    "address": "Rue de Wololo"
                    "category": "cleanup"
                    "time": "2012-04-23T18:25:43.511Z"
                    "id": 420
                },
            ]
    }
    return jsonify(list)


port = os.getenv('PORT', '5000')
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=int(port))
