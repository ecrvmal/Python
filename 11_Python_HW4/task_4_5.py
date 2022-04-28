import utils
import sys

curr = sys.argv[1:]         # collect argues
#   print(curr)             # debug print

                            # check each argue
for el in curr:
    out1 = utils.currency_rates('http://www.cbr.ru/scripts/XML_daily.asp', el )
    if out1:
            rate, nom = out1
            print(f"{nom} {el.upper()} равен {rate} рублей ")
    else:
            print(f" Currency {el.upper()}  if not found ")

