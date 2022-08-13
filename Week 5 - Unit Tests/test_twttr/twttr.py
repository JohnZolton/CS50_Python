# remove vowels from str input
def main():
    text =  input('enter your tweet: ')
    x = shorten(text)
    print(x)

def shorten(text):
    x = text
    x = x.replace('a','')
    x = x.replace('e','')
    x = x.replace('i','')
    x = x.replace('o','')
    x = x.replace('u','')
    x = x.replace('A','')
    x = x.replace('E','')
    x = x.replace('I','')
    x = x.replace('O','')
    x = x.replace('U','')
    return x


if __name__=="__main__":
    main()