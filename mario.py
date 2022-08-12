# TODO
from cs50 import get_int

def main():
    n=get_height()
    x=1
    for j in range(n):
        for i in range(n-x):
            print(" ", end="")
        for j in range(x):
            print("#", end="")
        x=x+1
        print()

def get_height():
    while True:
        n=get_int("height: ")
        if (n>0 and n<9):
            break
    return n

main()