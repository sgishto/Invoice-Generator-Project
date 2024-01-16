# invoice-generator

This is a full description of what this project should do and what modifications need to be done in order for the project to work on your system

First, you need to download this library from your terminal use the underneath command: 
pip install fillpdf

- (https://pypi.org/project/fillpdf/) <- This is the documentation of the library


Now we will go through each Python file we have and list the required changes: 

1- random_ids.py: 

line 7: df = pd.read_csv('csv/data2023.csv'): change the CSV location accordingly

2- reg.py:

line 6 to line 9: you can delete the single quotations and make the system run without making the user enter a month (NOTE: this code will only generate invoices for data within the current month you are running it for)

If you want to make the month insertion manual by the user, keep lines 6 to 9 commented. 

line 16: df = pd.read_csv('csv/data2023.csv'): change the CSV location accordingly 

line 24: mask = dfID["Round_Month(Datum)"].str.startswith(date_without_day): change date_without_day to (The_date_for_ivoice) only if you are running line 6 to line 9



3- TestAPI.py:

If you are going to uncomment lines 6 to 9 from the previous file (reg.py), then follow the next instructions, otherwise you can skip:
line 7: uncomment (#,today)
line 76: row = df.loc[month]: replace (month) with (today)



4- compareParktype.py:

line 5: df = pd.read_csv('csv/Plantdata(Park_type).csv') < change the CSV location accordingly 

line 21 to line 32: change the names between the brackets based on the names of the columns you have on your CSV file, for example in line 26: thegutschrift = test["Gutschriftnummer"].iloc[0]: change (Gutschriftnummer) to the name of the column for the Gutschriftnummer



5- pricebasedonparktype.py:

line 6 and line 7: change the CSV location accordingly 



6- testingcombin.py:

line 16: change the CSV location accordingly 



Notice: running the code should be from the testingcombin.py file









