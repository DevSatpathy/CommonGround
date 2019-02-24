from flask import Flask, render_template
from flask import request
import pymongo
from pymongo import MongoClient
from .backend.aggregation.closestlocation import get_midpoint, get_closest_building, get_random_code
import json

app = Flask(__name__)
#app._static_folder = './templates'

# Connect to the client
client = MongoClient('localhost', 27017)

# Connect to the database
db = client.commonground

# The collection that we will edit
rooms = db.rooms

@app.route("/")
def main_page():
	return render_template('MainPage.html')

@app.route("/joinroom")
def joinroom():
    return render_template('joinform.html')
    
@app.route("/createroom", methods=['PUT'])
def createroom():
    name = request.args.get('name')
    room_name = request.args.get('room_name')
    ip_address = request.args.get('ip_address')
    x_pos = request.args.get('x')
    y_pos = request.args.get('y')
    room_code = get_random_code()
    rooms.insertOne(
        {
            "name": room_name,
            "code": room_code,
            "users": [{"name": name, "x": x_pos, "y": y_pos, "ip": ip_address}],
            "meeting_location": {
                "name": 3,
                "x": 3,
                "y": 3
            }
        }
    )
    return render_template('CreateRoom.html')


@app.route("/results/<code>")
def output_data(code):
	return rooms.find({"code": code})
