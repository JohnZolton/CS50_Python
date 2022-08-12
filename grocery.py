list = {}
while True:
    try:

        item = input().strip().upper()
        if item not in list.keys():
            list[item] = 1
        else:
            list[item] +=1
    except EOFError:
        for key, value in sorted(list.items()):
            print(value, key)
        print()
        break
    except KeyError:
        continue