while  True:
    date  = input('Date: ').strip().title()

    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    try:
    #TODO add in try and excepts
        if date[0].isdigit():
            # date  is MM/DD/YYYY
            month, day, year = date.split(sep='/')
            month = int(month)
            day = int(day)
            if month <= 12 and day <= 31 and month >=1 and day >=1:
                print(f'{year}-{month:02}-{day:02}')
                break
        else:
            # date is Month day, year
            month, day, year = date.split(sep=' ')
            x = len(day)-1
            day = day[0:x] # delete the comma
            day = int(day)
            #  convert month name to number
            month = months.index(month)+1
            if int(month) <= 12 and int(day) <= 31:
                print(f'{year}-{month:02}-{day:02}')
                break
    except:
        print()
        pass