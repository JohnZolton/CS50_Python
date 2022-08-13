text =  input('enter your tweet: ').strip()

for i in text:
    if i.lower()== 'a' or i.lower()=='e' or i.lower()=='i' or i.lower()=='o' or i.lower()== 'u':
        print('', sep='', end ='')
    else:
        print(i, sep= '', end='')
print()