from flask import Flask, render_template, redirect, url_for
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

@app.route("/joinroom", methods = ['POST', 'GET'])
def joinroom():
    if request.method == 'POST':
        result  = request.form
        name = result['name']
        lat = result['xcoord']
        lon = result['ycoord']
        code = result['code']
        ip_address = 0
        
        # current_users = rooms.find_one({ 'code':code}, {'_id': 0, 'name': 0, 'users': 1, 'meeting_loc': 0})
        # for i in range(len(current_users)):
        #     if current_users[i]['ip_address'] == ip_address:
        #         current_users[i] = { "ip": ip_address,
        #                 "name": name,
        #                 "x": lat,
        #                 "y": lon
        #                 }
        #     else:
        #         current_users.append({ "ip": ip_address,
        #                 "name": name,
        #                 "x": lat,
        #                 "y": lon
        #                 })
        
        # rooms.update_one({"code":code},{ "$set":{"users": current_users}})
        # current_users = rooms.find_one({ 'code':code}, {'_id': 0, 'name': 0, 'users': 1, 'meeting_loc': 0})
        # coords = []
        # for i in range(current_users):
        #     coords.append((current_users[i]['x'],current_users[i]['y']))
        # meeting_location = get_midpoint(coords)
        # meeting_location_x = meeting_location[0]
        # meeting_location_y = meeting_location[1]
        # meeting_building = get_closest_building(meeting_location_x, meeting_location_y)
        # rooms.update_one({"code":code},{ "$set":{"meeting_loc": {"name": meeting_building, "x": meeting_location_x, "y": meeting_location_y}}})
        return redirect(url_for('results', code=3))
    else:
        return render_template('joinform.html')
    
@app.route("/createroom", methods=['POST', 'GET'])
def createroom():
    print('bye')
    if request.method == 'POST':
        print(85)
        result  = request.form
        name = result['name']
        lat = result['xcoord']
        lon = result['ycoord']
        print('hello')
        code = get_random_code()
        print('hello')
        meeting_building = get_closest_building(lat, lon)
        print(meeting_building[2])

        ip_address = 0
        db.rooms.insert(
            {
                "name": name,
                "code": code,
                "users": [{"name": name, "x": lat, "y": lon, "ip": ip_address}],
                "meeting_location": {
                    "name": meeting_building[0],
                    "x": meeting_building[1],
                    "y": meeting_building[2]}
            }
        )
        print('asdfasdf')
        return redirect(url_for('results', code=code))
    else:
        return render_template('CreateRoom.html')


@app.route("/results/<code>")
def results(code):
	# return rooms.find({"code": code})
    data = rooms.find({'code': code})
    dat = str(data)
    with open('users.json', 'w') as outfile:  
        json.dump(dat, outfile)
    return render_template('Result.html')
