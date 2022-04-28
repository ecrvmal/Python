import utils
import sys

currencies = ["usd" , "CHf" , "uZs" , "tJs", "check" ]


# main()
print('  WELCOME TO CURRENCY CONVERTER PROGRAMM \n ')
print(f' Checking Currencies : {currencies}  \n')

print ('\n   Module "currency_rates" \n')

for currency in currencies:
        out1 = utils.currency_rates('http://www.cbr.ru/scripts/XML_daily.asp', currency )
        if out1:
                rate, nom = out1
                print(f"{nom} {currency.upper()} равен {rate} рублей ")
        else:
                print(f" Currency {currency.upper()}  if not found ")

print ('\n   Module "currency_rates_advanced" \n')
for currency in currencies:
        out1 = utils.currency_rates_advanced('http://www.cbr.ru/scripts/XML_daily.asp', currency )
        if out1:
                rate, nom, date1 = out1
                print(f"{nom} {currency.upper()} равен {rate} рублей на дату {date1}")
        else:
                print(f" Currency {currency.upper()}  if not found ")

