import inflect
p = inflect.engine()
names = []

#get some names from the user
while True:
    try:
        name  = input('Name: ')
        names.append(name)

    except EOFError:
        #ctl+D to stop
        print()
        break
mylist = p.join((names))
print('Adieu, adieu, to '+ mylist)
