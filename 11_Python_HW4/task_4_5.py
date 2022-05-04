import utils
import sys

curr = sys.argv[1:]         # collect argues
#   print(curr)             # debug print

                            # check each argue

out1 = utils.currency_rates('http://www.cbr.ru/scripts/XML_daily.asp', curr[0] )
if out1:
        rate, nom = out1
        print(f"{nom} {curr[0].upper()} равен {rate} рублей ")
else:
        print(f" Currency {curr[0].upper()}  if not found ")

