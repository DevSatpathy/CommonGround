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
        # ip_address = 0

        text = open('users.json', 'r')
        rooms = json.loads(text.read())
        coords = []
        user = {'name': name, 'x': lat, 'y': lon}
        inside = False

        for i in range(len(rooms)) and not inside:

            if rooms[i]['code'] is code:
                for j in range(len(rooms[i]['users'])):
                    coords.append((rooms[i]['users'][j]['x'], rooms[i]['users'][j]['y']))

                    if rooms[i]['users']['name'] is user['name']:
                        inside = True
                        rooms[i]['users']['x'] = user['x']
                        rooms[i]['users']['y'] = user['y']
        
        if not inside:
            rooms[i]['users'].append(user)

        with open('users.json', 'w') as outfile:  
            json.dump(rooms, outfile)

        
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
        

        # user = {
        #         "name": name,
        #         "code": code,
        #         "users": [{"name": name, "x": lat, "y": lon, "ip": ip_address}],
        #         "meeting_location": {
        #             "name": meeting_building[0],
        #             "x": meeting_building[1],
        #             "y": meeting_building[2]}
        #     }
        # rooms.update_one({"code":code},{ "$set":{"users": current_users}})
        # current_users = rooms.find_one({ 'code':code}, {'_id': 0, 'name': 0, 'users': 1, 'meeting_loc': 0})
        # coords = []
        # for i in range(current_users):
        #     coords.append((current_users[i]['x'],current_users[i]['y']))
        meeting_location = get_midpoint(coords)
        meeting_location_x = meeting_location[0]
        meeting_location_y = meeting_location[1]
        meeting_building = get_closest_building(meeting_location_x, meeting_location_y)
        text.close()
        # rooms.update_one({"code":code},{ "$set":{"meeting_loc": {"name": meeting_building, "x": meeting_location_x, "y": meeting_location_y}}})
        # user = {{"code":code},{ "$set":{"users": current_users}},{"code":code},{ "$set":{"meeting_loc": {"name": meeting_building, "x": meeting_location_x, "y": meeting_location_y}}}}
        return redirect(url_for('results', location=meeting_building[0]))
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
        return redirect(url_for('results', location=meeting_building[0]))
    else:
        return render_template('CreateRoom.html')


@app.route("/results/<location>")
def results(location):

    return render_template('Result.html')
