import pandas as pd
from reg import result_dict, first_date, last_date
from pricebasedonparktype import Contracttype, performance, priceperkwh, totalprice
from datetime import datetime
from fillpdf import fillpdfs

df = pd.read_csv('csv/data2023.csv')
fields = fillpdfs.get_form_fields("Examplary Invoice.pdf")

Gutschriftsnummer = "RRDV9999"
datum = datetime.today().strftime("%d.%m.%Y")
Kundennummer = 5000
SteuerID = "555/000/333"
Parkname_Marke = "AMP-101-507"
Zeitraum = f'{first_date}-{last_date}'
Parkname_Kunde = "Hagen_AMP"
Marktlokation = 105010
Rechnungsnummer = "RRDV9999"
Abregelungsverguetung_Mark_E = 0.01

for i, value in result_dict.items():
    data_dict = {
        "Gutschriftsnummer": Gutschriftsnummer,
        "Datum": datum,
        "Kundennummer": Kundennummer,
        "SteuerID": SteuerID,
        "Zeitraum": Zeitraum,
        "Parkname_Marke": Parkname_Marke,
        "Marktlokation": Marktlokation,
        "Rechnungsnummer": Rechnungsnummer,
        "Abregelungsverguetung_Mark-E": Abregelungsverguetung_Mark_E,
        "Einspeisemenge": value
    }

    for keyofprice, valueofprice in priceperkwh.items():
        if keyofprice == i:
            MW_Anlage_Verguetung = valueofprice
            MW_tecbnologie_Verguetung = valueofprice
            data_dict['MW_Anlage_Verguetung'] = MW_Anlage_Verguetung
            data_dict['MW_tecbnologie_Verguetung'] = MW_tecbnologie_Verguetung

            for keyoftotalprice, valueoftotalprice in totalprice.items():
                if keyoftotalprice == keyofprice:
                    Summe_Anlagen_MW = valueoftotalprice
                    Nettobetrag_G = valueoftotalprice
                    SUMME_Steuer = round(float(Nettobetrag_G) + (float(Nettobetrag_G) * 0.19), 2)
                    Bruttobetrag_G = SUMME_Steuer
                    data_dict['Summe_Anlagen_MW'] = Summe_Anlagen_MW
                    data_dict['Nettobetrag_G'] = Nettobetrag_G
                    data_dict['SUMME_Steuer'] = SUMME_Steuer
                    data_dict['Bruttobetrag_G'] = Bruttobetrag_G

                    for contractkey, contract in Contracttype.items():
                        if contractkey == keyoftotalprice:
                            for keyperformance, per in performance.items():
                                if keyperformance == contractkey:
                                    if contract == "standard_post" and per > 0:
                                        fillpdfs.write_fillable_pdf('updated invoices/Performance and standard.pdf', f'invoices/{i}.pdf', data_dict)
                                        print(f"Printed {i} with performance and standard")
                                    elif contract == "standard_post" and per == 0:
                                        fillpdfs.write_fillable_pdf('updated invoices/no performance and standard.pdf', f'invoices/{i}.pdf', data_dict)
                                        print(f"Printed {i} with no performance and standard")
                                    elif contract != "standard_post" and per > 0:
                                        fillpdfs.write_fillable_pdf('updated invoices/performance without standard.pdf', f'invoices/{i}.pdf', data_dict)
                                        print(f"Printed {i} with performance and no standard")
                                    elif contract != "standard_post" and per == 0:
                                        fillpdfs.write_fillable_pdf('updated invoices/no performance and no standard.pdf', f'invoices/{i}.pdf', data_dict)
                                        print(f"Printed {i} with no performance and no standard")
                                    else:
                                        print("Not working")


