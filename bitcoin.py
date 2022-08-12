import requests
import json
import sys

#expect users to specify as a command-line argument the number of bitcoins they want
try:
    x = float(sys.argv[1])
except IndexError:
    sys.exit("Missing command-line argument")
except ValueError:
    sys.exit("Command-line argument is not a number")

r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')

o = r.json()
y = o['bpi']['USD']['rate_float']
z = x * y
print(f'${z:,.4f}')