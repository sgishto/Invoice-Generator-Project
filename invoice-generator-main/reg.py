import pandas as pd
import os
from random_ids import randomlist

df = pd.read_csv('csv/data2023.csv')
result_dict = {}
for theid in randomlist:
    mask2 = df[df["ZP_ID"] == theid]
    if not mask2.empty:
        filename = f"filteredbyID_{theid}.csv"
        mask2.to_csv(filename, index=False)
        dfID = pd.read_csv(filename)
        mask = dfID["Round_Month(Datum)"].str.startswith("2023-02")
        filtered_df = dfID[mask]
        filename = f"filteredbydate_{theid}.csv"
        filtered_df.to_csv(filename, index=False)
        df1 = pd.read_csv(filename)
        last_value = df1["Stunde_von"].iloc[0]
        last_date = last_value.split("T")[0]
        first_value = df1["Stunde_von"].iloc[-1]
        first_date = first_value.split("T")[0]
        sum_B = round(df1['Arbeit [kWh]'].sum(),2)
        result_dict[theid] = sum_B
        os.remove(filename)
        os.remove(f"filteredbyID_{theid}.csv")
    else:
        print(f"The ID {theid} does not exist")
#apply to see the data
print(f"result dict{result_dict}")
