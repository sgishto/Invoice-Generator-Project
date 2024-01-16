import pandas as pd
import random

df = pd.read_csv('csv/data2023.csv')

column_name_1 = "ZP_ID"
column_name_2 = "NAME_S"

randomlist = []

#Use a loop to select 5 random values from the column
for i in range(5):
    random_row_index = random.randint(0, len(df) - 1)
    if "Summenzählpunkt" in df.loc[random_row_index, 'NAME_S']:
        continue
    if df.loc[random_row_index, 'Spec'] == "1802":
        continue

    random_data = df.loc[random_row_index, column_name_1]

    randomlist.append(random_data)

#print(randomlist)
