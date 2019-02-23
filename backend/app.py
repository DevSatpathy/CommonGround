from flask import Flask
from flask import request
from pymongo import MongoClient
import pymongo
from aggregation.currentlocation import *
app = Flask(__name__)

# Connect to the database
client = MongoClient('localhost', 27017)

# The collection that we will edit
rooms = db.rooms

@app.route("/info", method=['PUT'])
def add_to_database():
    p = request.args.get('permissions')
    if p == "yes":
        curr_loc = aggregation.currentlocation.get_current_location()
    else:
        curr_loc = aggregation.currentlocation.get_current_location_from_address(request.args.get('address'))