def main():
    frac = input('enter a fraction (x/y): ')
    percent = convert(frac)
    reading = gauge(percent)
    print(reading)

def convert(fraction):
    while True:
        try:
            x, y = fraction.split(sep='/')
            x = int(x)
            y = int(y)
            z = x/y*100
            if z <= 100 and z >= 0:
                return z
            else:
                fraction = input('enter a fraction (x/y): ')
                pass
        except (ValueError, ZeroDivisionError):
            raise

def gauge(percentage):
    if percentage > 100:
        return "can't have over 100%"
    elif percentage <= 1:
        return 'E'
    elif percentage >= 99:
        return 'F'
    else:
        return f'{percentage:.0f}%'


if __name__=="__main__":
    main()

