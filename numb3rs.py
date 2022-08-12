import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    parts = ip.split('.')
    for part in parts:
        if not (part.isnumeric() and 0 <= int(part) and int(part) <= 255):
            return False
    return True


if __name__=="__main__":
    main()