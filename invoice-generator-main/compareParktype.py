import pandas as pd
from reg import result_dict

df = pd.read_csv('csv/Plantdata(Park_type).csv')
parktype = {}
for id in result_dict:
    try:
        test = df[df["meter_point_key"] == id]
        name = df["park_key"]
        thetype = test['park_type'].iloc[0]
        parktype[id] = thetype
    except IndexError:
        print("The ID: "+id+" Doesn't have a park type data")

print(f"park type: {parktype}")
