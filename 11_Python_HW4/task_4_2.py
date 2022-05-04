import requests

currencies = ["usd" , "CHf" , "uZs" , "tJs", "check" ]

def currency_rates(url, currency_code):
        response = requests.get(url)
        r = response.text.split("</Valute>")
        name = currency_code.upper();
        for n in r:
                # print(n)
                if name in n:
                        nominal_start = n.find('<Nominal>') + len('<Nominal>')
                        nominal_end = n.find('</Nominal>')
                        nominal = (int(n[nominal_start:nominal_end]))
                        # print(f'Nominal = {nominal}')
                        value_start = n.find('<Value>') + len('<Value>')
                        value_end = n.find('</Value>')
                        value = float( n[value_start:value_end].replace(',', '.'))
                        #print(f"{nominal} {name} равен {value} рублей")
                        output = (value, nominal)
                        return  output
        return


# main()



print('  WELCOME TO CURRENCY CONVERTER PROGRAMM \n ')
print(f' Checking Currencies : {currencies}  \n')

for currency in currencies:
        out1 = currency_rates('http://www.cbr.ru/scripts/XML_daily.asp', currency )
        if out1:
                rate, nom = out1
                print(f"{nom} {currency.upper()} равен {rate} рублей")
        else:
                print(f" Currency {currency.upper()}  if not found ")

