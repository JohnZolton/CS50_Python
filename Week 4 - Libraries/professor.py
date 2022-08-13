import random

def main():
    level = get_level()
    list1=[]
    list2=[]
    for i in range(10):
        list1.append(generate_integer(level))
        list2.append(generate_integer(level))

    score = 0
    for i in range(10):
        tries = 3
        while tries > 0:
            try:
                ans = int(input(f'{list1[i]} + {list2[i]} = '))
            except ValueError:
                tries += -1
                print('EEE')
                continue
            if ans != list1[i] + list2[i]:
                print('EEE')
                tries += -1
            else:
                score +=1
                break


            if tries == 0:
                print(f'{list1[i]} + {list2[i]} = ', list1[i]+list2[i])

    print('Score: ', score)


def get_level():
    while True:
        try:
            level = input('Level: ')
            level=int(level)
            if level in [1, 2, 3]:
                return level
        except ValueError:
            continue

def generate_integer(level):
    if level ==1:
        x = random.randint(0,9)
    elif level ==2:
        x = random.randint(10,99)
    else:
        x = random.randint(100,999)
    return x




if __name__=="__main__":
    main()