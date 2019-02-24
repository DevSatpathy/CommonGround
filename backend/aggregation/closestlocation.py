import pandas as pd
import math
import random
# from currentlocation import *

df = pd.read_csv('backend/aggregation/data/location_gps.csv', sep =';', error_bad_lines=False)

d =  df.set_index('name').to_dict(orient = 'series')

def distance_from_user(name, user_x, user_y):
    # data = d.get(name)
    # x = data.get('x_coord')
    # y = data.get('y_coord')
    # print(df)
    x = float(df[df['name']==name]['x_coord'])
    y = float(df[df['name']==name]['y_coord'])
    dist = math.sqrt((user_x - x)**2 + (user_y - y)**2)
    return dist

def get_midpoint(user_coords): # user_coords is a list of tuples storing all x, y gps coordinates
    num_users = len(user_coords)
    print("num user: " + str(num_users))
    y_sum = 0
    x_sum = 0
    for i in range(num_users):
        x_sum += float(user_coords[i][0])
        y_sum += float(user_coords[i][0])
    return ((x_sum / num_users), (y_sum / num_users))

def get_closest_building(x_coord, y_coord):
    min_dist = float("inf")
    name = ""
    x = 0
    y = 0
    for n in df['name']:
        dist = distance_from_user(n, float(x_coord), float(y_coord))
        if (dist < min_dist):
            min_dist = dist
            name = n
            x = float(df[df['name']==n]['x_coord'])
            y = float(df[df['name']==n]['y_coord'])
    return [name, x, y]

def get_random_code():
    chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXTZabcdefghiklmnopqrstuvwxyz"
    string_length = 5
    randomstring = ''
    for i in range(6):
        rnum = random.randint(0,len(chars))
        randomstring += chars[rnum:rnum+1]
    
    return randomstring

# get midpoint for list of coordinates
# compare the midpoint with all buildings (in location_gps.csv)
    # return the closest building / address
    
# user_location = getCurrentLocation()
# print(distance_from_user('Cocomero', user_location[0], user_location[1]))
