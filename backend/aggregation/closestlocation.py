import pandas as pd

df = pd.read_csv('data/location_gps.csv', sep =';', error_bad_lines=False)

d =  df.set_index('name').to_dict(orient = 'index')

def closest_loc(name):
    x = d.get(name);

print(d['Cocomero'])