import geocoder
import pandas as pd

def generate_coordinates():
    print("Reading csv...")
    # df = pd.read_csv("data/common_ground_data.csv", error_bad_lines=False, sep=';')
    df = pd.read_csv("backend/aggregation/data/common_ground_data.csv", error_bad_lines=False, sep=';')
    location_gps = open("backend/aggregation/data/location_gps.csv", "w+")
    # location_gps = open("data/location_gps.csv", "w+")

    for col in (df.columns.values):
        location_gps.write(col + ";")
    location_gps.write("x_coord;y_coord\n")

    print("Getting all gps coordinates...")
    for i, row in df.iterrows():

        category = df.loc[i,'category']
        building = df.loc[i, 'name']
        address = df.loc[i, 'address']
        g = geocoder.osm(address)
        
        try:
            info_str = building + ";" + category + ";" + address + ";" + str(g.osm['x']) + ";" + str(g.osm['y']) + "\n"
            location_gps.write(info_str)
        except:
            print("There is an invalid address...skipping over...")

    print("Finished getting all gps coordinates...")

    location_gps.close()   
# generate_coordinates() 