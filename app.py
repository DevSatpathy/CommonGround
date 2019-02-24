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

        text = open('users.json', 'r')
        rooms = json.loads(text.read())
        coords = []
        user = {'name': name, 'x': lat, 'y': lon}
        inside = False
        print("rooms")
        print(len(rooms))
        if len(rooms) == 0:
            render_template('joinform.html')
        for i in range(len(rooms)):
            if rooms[i]['code'] == code:
                print("yes")
                for j in range(len(rooms[i]['users'])):
                    print("line 46")
                    print("another user")
                    coords.append((rooms[i]['users'][j]['x'], rooms[i]['users'][j]['y']))

                if rooms[i]['users'][j]['name'] == user['name']:
                    print("line 51")
                    inside = True
                    rooms[i]['users'][j]['x'] = user['x']
                    rooms[i]['users'][j]['y'] = user['y']
                    coords.append((user['x'], user['y']))
        
                if not inside:
                    print("line 58")
                    rooms[i]['users'].append(user)
                    coords.append((user['x'], user['y']))

        with open('users.json', 'w') as outfile:  
            json.dump(rooms, outfile)

        print(coords)

        meeting_location = get_midpoint(coords)
        meeting_location_x = meeting_location[0]
        meeting_location_y = meeting_location[1]
        meeting_building = get_closest_building(meeting_location_x, meeting_location_y)
        text.close()

        return redirect(url_for('results', location=meeting_building[0]), code = code)
    else:
        return render_template('joinform.html')
    
@app.route("/createroom", methods=['POST', 'GET'])
def createroom():
    if request.method == 'POST':
        result  = request.form
        name = result['name']
        roomname = result['roomname']
        lat = result['xcoord']
        lon = result['ycoord']
        code = get_random_code()
        meeting_building = get_closest_building(lat, lon)
        # ip_address = 0
        # db.rooms.insert_one(
        #     {
        #         "name": name,
        #         "code": code,
        #         "users": [{"name": name, "x": lat, "y": lon, "ip": ip_address}],
        #         "meeting_location": {
        #             "name": meeting_building[0],
        #             "x": meeting_building[1],
        #             "y": meeting_building[2]}
        #     }
        # )
        text = open('users.json', 'r')
        # rooms = json.load(text.read())
        rooms = json.load(text);

        room = {
                "name": roomname,
                "code": code,
                "users": [{"name": name, "x": lat, "y": lon}]}

        rooms.append(room)
                                                                                              
        with open('users.json', 'w') as outfile:  
            json.dump(rooms, outfile)
        text.close()
        return redirect(url_for('results', location=meeting_building[0]), code = code)
    else:
        return render_template('CreateRoom.html')


@app.route("/results/<location>")
def results(location, code):
    
    return render_template('Result.html', location = location, code = code)
