while True:
    try:
        x, y = input('enter a fraction (X/Y): ').split(sep="/")
        x = int(x)
        y = int(y)
        z = x/y*100
        if z > 100:
            print("can't have over 100%")
        elif z <= 1:
            print("E")
            break
        elif z >= 99:
            print('F')
            break
        else:
            print(f'{z:.0f}%')
            break
    except ValueError:
            print("must be an interger")
    except ZeroDivisionError:
        print("can't divide by zero")








