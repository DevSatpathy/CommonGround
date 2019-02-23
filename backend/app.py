from flask import Flask
from flask import request
import pymongo
from pymongo import MongoClient
from aggregation.currentlocation import *
app = Flask(__name__)

# Connect to the client
client = MongoClient('localhost', 27017)

# Connect to the database
db = client.commonground

# The collection that we will edit
rooms = db.rooms

@app.route("/joinroom", methods=['POST'])
def joinroom():
    name = request.args.get('name')
    if long == -1:
        
    long = request.args.get('longitude', type=int)
    lat = request.args.get('latitude', type=int)
    code = request.args.get('code')
    ip_address = request.args.get('ip_address')
    address = request.args.get('address')
    current_users = rooms.find_one({ 'code':code}, {'_id': 0, 'name': 0, 'users': 1, 'meeting_loc': 0})
    for i in range(len(current_users)):
        if current_users[i]['ip_address'] == ip_address:
            current_users[i] = { "ip": ip_address,
                    "name": name,
                    "x": lat,
                    "y": long,
                    "address": address }
        else:
            current_users.append({ "ip": ip_address,
                    "name": name,
                    "x": lat,
                    "y": long,
                    "address": address })
    rooms.update_one(
            {"code":code},
            { "$set":{
                    "users": current_users
                    }
            }
        )
        
@app.route("/createroom", methods=['PUT'])
def createroom():
    name = request.args.get('name')
    ip_address = request.args.get('ip_address')
    
@app.route("/results/<code>")
def output_data(code):
	return rooms.find({"code": code})
