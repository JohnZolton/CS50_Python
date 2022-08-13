def convert(phrase):
    phrase = phrase.replace(':)','🙂').replace(':(','🙁')
    print(phrase)

x = input()
y = convert(x)
