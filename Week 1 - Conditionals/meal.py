def main():
    time = input('what time is it? ').strip()
    hours,  minutes = convert(time)
    if hours == '7' or (hours == '8' and minutes =='00'):
        print('breakfast time')
    elif hours == '12' or (hours == '13' and minutes =='00'):
        print('lunch time')
    elif hours == '18' or (hours == '19' and minutes =='00'):
        print('dinner time')


def convert(time):
    hours, minutes = time.split(':')
    return hours, minutes


if __name__ == "__main__":
    main()