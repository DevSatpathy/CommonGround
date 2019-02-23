import geocoder
import pandas as pd

df = pd.read_csv("data/common_ground_data.csv", error_bad_lines=False, sep=';')

print(df)
# g = geocoder.osm('1408 W Gregory Dr, Urbana, IL 61801')
# g.json
# print(g.osm)