import sys
from tabulate import tabulate
import csv

if not sys.argv[1].endswith(".csv"):
    sys.exit('Not a CSV file')

if len(sys.argv) == 2:
    try:
        menu = []
        with open(sys.argv[1]) as file:
            reader = csv.reader(file)
            for row in reader:
                menu.append(row)
            print(tabulate(menu[1:], headers=menu[0], tablefmt='grid'))

    except FileNotFoundError:
        sys.exit('File does not exist')
elif len(sys.argv) > 2:
    sys.exit('Too many command-line arguments')

else:
    sys.exit('Too few command-line arguments')

