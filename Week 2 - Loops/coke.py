total = 0
due = 50
while True:
    coin = int(input('enter a coin: '))
    if coin == 5 or coin == 10 or coin == 25:
        total += coin
        due = 50 - total
    if due > 0:
        print(due)
    if total >= 50:
        change = total - 50
        print('change owed: ', change)
        break