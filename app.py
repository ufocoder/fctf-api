import json

from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

isOK = {'result': True}
isBad = {'result': False}
isFlag = {'result': True, 'url': 'https://docs.google.com/forms/d/e/1FAIpQLSd499vDqDUkOPa6cp8uT4ZBfVqQ3E0_elafZJezK_9Pi4J1Jg/viewform'}

with open('tasks.json') as json_file:
    tasks = json.load(json_file)

with open('flags.json') as json_file:
    flags = json.load(json_file)

@app.route("/")
def home():
    return "ayy lmao"


@app.route("/data")
def data():
    return jsonify(tasks)


@app.route('/colonize', methods=['POST'])
def colonize():
    planetId = str(request.json['planetId'])
    flag = str(request.json['flag']).lower()

    if flags.get(planetId) == flag:
        return isOK

    return isBad


def lower(item):
    return (item[0], item[1].lower())

@app.route('/check', methods=['POST'])
def check():
    requestFlags = dict(map(lower, request.json['flags'].items()))
    if requestFlags == flags:
        return isFlag            

    return isBad
