import requests
import datetime

currencies = ["usd" , "CHf" , "uZs" , "tJs", "check" ]

def currency_rates_advanced (url, currency_code):
        response = requests.get(url)
        r = response.text.split("</Valute>")

        date1 = datetime.date.today()
        # print(date1)

        name = currency_code.upper();
        for n in r:
                # print(n)

                if name in n:
                        nominal_start = n.find('<Nominal>') + len('<Nominal>')  #       start position of nominal
                        nominal_end = n.find('</Nominal>')                      #      end position of nominal
                        nominal = (int(n[nominal_start:nominal_end]))
                        # print(f'Nominal = {nominal}')
                        value_start = n.find('<Value>') + len('<Value>')
                        value_end = n.find('</Value>')
                        value = float( n[value_start:value_end].replace(',', '.'))
                        #print(f"{nominal} {name} равен {value} рублей")
                        output = (value, nominal, date1)
                        return  output
        return


# main()
print('  WELCOME TO CURRENCY CONVERTER PROGRAMM \n ')
print(f' Checking Currencies : {currencies}  \n')

for currency in currencies:
        out1 = currency_rates_advanced('http://www.cbr.ru/scripts/XML_daily.asp', currency )
        if out1:
                rate, nom, date1 = out1
                print(f"{nom} {currency.upper()} равен {rate} рублей на дату {date1}")
        else:
                print(f" Currency {currency.upper()}  if not found ")

