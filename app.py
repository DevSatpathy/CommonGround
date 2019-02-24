from flask import Flask, render_template
from flask import request
import pymongo
from pymongo import MongoClient
from .backend.aggregation.closestlocation import get_midpoint, get_closest_building
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

@app.route("/JoinRoom.html", methods=['POST'])
def joinroom():
    name = request.args.get('name')
    lon = request.args.get('longitude', type=int)
    lat = request.args.get('latitude', type=int)
    code = request.args.get('code')
    ip_address = request.args.get('ip_address')
    current_users = rooms.find_one({ 'code':code}, {'_id': 0, 'name': 0, 'users': 1, 'meeting_loc': 0})
    for i in range(len(current_users)):
        if current_users[i]['ip_address'] == ip_address:
            current_users[i] = { "ip": ip_address,
                    "name": name,
                    "x": lat,
                    "y": lon
                    }
        else:
            current_users.append({ "ip": ip_address,
                    "name": name,
                    "x": lat,
                    "y": lon
                    })
    
    rooms.update_one({"code":code},{ "$set":{"users": current_users}})
    current_users = rooms.find_one({ 'code':code}, {'_id': 0, 'name': 0, 'users': 1, 'meeting_loc': 0})
    coords = []
    for i in range(current_users):
        coords.append((current_users[i]['x'],current_users[i]['y']))
    meeting_location = get_midpoint(coords)
    meeting_location_x = meeting_location[0]
    meeting_location_y = meeting_location[1]
    meeting_building = get_closest_building(meeting_location_x, meeting_location_y)
    rooms.update_one({"code":code},{ "$set":{"meeting_loc": {"name": meeting_building, "x": meeting_location_x, "y": meeting_location_y}}})
    return render_template('Result.html')
    
@app.route("/createroom", methods=['PUT'])
def createroom():
	name = request.args.get('name')
	room_name = request.args.get('room_name')
	ip_address = request.args.get('ip_address')
	x_pos = request.args.get('x')
	y_pos = request.args.get('y')
	rooms.insertOne(
		{"name": room_name,
		"code": 3,
		"users": [{"name": name, "x": x_pos, "y": y_pos, "ip": ip_address}],
		"meeting_location": {
			"name": 3,
			"x": 3,
			"y": 3}})


@app.route("/results/<code>")
def output_data(code):
	return rooms.find({"code": code})
