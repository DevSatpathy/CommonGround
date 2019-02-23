from flask import Flask
from flask import request
import pymongo
from pymongo import MongoClient
from aggregation.currentlocation import *
app = Flask(__name__)

# Connect to the client
client = MongoClient('localhost', 27017)

# Connect to the database
db = client.db

# The collection that we will edit
rooms = db.rooms

@app.route("/joinroom")
def join_room():
    name = request.args.get('name')
    long = request.args.get('longitude')
    lat = request.args.get('latitude')
    code = request.args.get('code')
    ip_address = request.args.get('ip_address')
    info = { "ip": ip_address, "longitude": long, "latitude": lat }
    rooms.insert_one(info)

@app.route("/createroom")
def create_room():
    name = request.args.get('name')
    ip_address = request.args.get('ip_address')
    
@app.route("/results/<code>")
def output_data(code):
	return rooms.find({"code": code})