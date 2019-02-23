import pandas as pd

df = pd.read_csv('data/common_ground_data.csv', sep =';', error_bad_lines=False)

d =  df.set_index('name').to_dict(orient = 'index')


print(d['Cocomero'])