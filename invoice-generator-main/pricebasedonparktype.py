from compareParktype import parktype
import pandas as pd
from reg import result_dict

df = pd.read_csv('csv/contract.csv')
dfParktype = pd.read_csv("csv/Plantdata(Park_type).csv")
Contracttype = {}
performance = {}
priceperkwh = {}
totalprice = {}
pricebasedontype = {}
pricebase = {'solar': 0.8002, 'hydropower': 0.10074,'landfill': 0.10074, 'biomass': 0.10074, 'wind': 0.8940, 'cogeneration': 0.10074}

def findthetotal (spending, id, price, performance):
    for key, value in spending.items():
        if key == id:
            if performance.get(key, 0) > 0:
                total = float(value) * price * 0.80
                priceperkwh[id]=price
                totalprice[id]= round(total,2)
            else:
                total = float(value) * 0.10074
                priceperkwh[id] = 0.10074
                totalprice[id] = round(total,2)
    return round(total, 2)

def verguetung (price_per_kwh):
    print(price_per_kwh)
    return price_per_kwh



def findthetype():
    for key, value in parktype.items():
        if value in pricebase:
            priceperkwh = pricebase[value]
            findthetotal(result_dict, key, priceperkwh, performance)


def findstandardcontract():
    for id in parktype:
        if id in df['meter_point_key'].values:
            contractlist = df[df["meter_point_key"] == id]
            contract_type = contractlist['contract_type'].iloc[0]
            Contracttype[id] = contract_type

def findperformance():
    for id in parktype:
        if id in dfParktype["meter_point_key"].values:
            performancelist = dfParktype[dfParktype["meter_point_key"] == id]
            performance_type = performancelist['Performance'].iloc[0]
            performance[id] = performance_type

findperformance()
findthetype()
findstandardcontract()
print(Contracttype)
print(f"performance: {performance}")
print(f'total price{totalprice}')
print(f'price per kwh {priceperkwh}')
# Print the value


'''
        elif value == "hydropower":
            priceperkwh = 0.8955
            findthetotal(result_dict, key, priceperkwh)

        elif value == "landfill":
            priceperkwh = 0.8515
            findthetotal(result_dict, key, priceperkwh)

        elif value == "biomass":
            priceperkwh = 0.10252
            findthetotal(result_dict, key, priceperkwh)

        elif value == "wind":
            priceperkwh = 0.8955
            findthetotal(result_dict, key, priceperkwh)

        elif value == "cogeneration":
            priceperkwh = 0.10252
            findthetotal(result_dict, key, priceperkwh)
        else:
            print("park type not available")
'''


