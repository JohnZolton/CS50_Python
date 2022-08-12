# TODO
from cs50 import get_float


cents=-1
while cents <0:
        cents = get_float("what is your change? ")
cents = int(cents*100)
coin_count = 0
while cents >= 25:
    cents = cents - 25
    coin_count=coin_count+1
while cents >=10:
    cents = cents - 10
    coin_count=coin_count+1
while cents >=5:
    cents = cents - 5
    coin_count=coin_count+1
while cents > 0:
    cents = cents - 1
    coin_count=coin_count+1
print(coin_count)