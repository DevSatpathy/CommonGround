import geocoder
import pandas as pd

df = pd.read_csv("data/common_ground_data.csv", error_bad_lines=False, sep=';')
location_gps = open("data/location_gps.csv", "w+")
for col in (df.columns.values):
    location_gps.write(col + ";")
location_gps.write("x_coord;y_coord\n")

for i, row in df.iterrows():

    category = df.loc[i,'category']
    building = df.loc[i, 'name']
    address = df.loc[i, 'address']
    g = geocoder.osm(address)
    
    try:
        info_str = category + ";" + building + ";" + address + ";" + str(g.osm['x']) + ";" + str(g.osm['y']) + "\n"
        location_gps.write(info_str)
    except:
        print("invalid address")

location_gps.close()
    