import pandas as pd
import math
from currentlocation import *

df = pd.read_csv('data/location_gps.csv', sep =';', error_bad_lines=False)

d =  df.set_index('name').to_dict(orient = 'index')

def distance_from_user(name, user_x, user_y):
    data = d.get(name)
    x = data.get('x_coord')
    y = data.get('y_coord')
    dist = math.sqrt((user_x - x)**2 + (user_y - y)**2)
    return dist

def get_midpoint(user_coords): # user_coords is a list of tuples storing all x, y gps coordinates
    num_users = len(user_coords)
    y_sum = 0
    x_sum = 0
    for i in range(num_users):
        x_sum += user_coords[i][0]
        y_sum += user_coords[i][0]
    return ((x_sum / num_users), (y_sum / num_users))

def get_closest_building(x_coord, y_coord):
    min_dist = float("inf")
    name = ""
    for n in df['name']:
        dist = distance_from_user(n, x_coord, y_coord)
        if (dist < min_dist):
            min_dist = dist
            name = n
    return name

# get midpoint for list of coordinates
# compare the midpoint with all buildings (in location_gps.csv)
    # return the closest building / address
    
# user_location = getCurrentLocation()
# print(distance_from_user('Cocomero', user_location[0], user_location[1]))
