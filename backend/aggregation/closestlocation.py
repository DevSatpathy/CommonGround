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
    
user_location = getCurrentLocation()
print(distance_from_user('Cocomero', user_location[0], user_location[1]))
