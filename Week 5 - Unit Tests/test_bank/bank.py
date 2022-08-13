def main():
    greeting = input("tell me a greeting: ")
    result = value(greeting)
    print(f'${result}')
def value(greeting):
    y = greeting.lower().strip()
    if y[0:5] == "hello":
        x = 0
        return x
    elif y[0] == "h":
        x = 20
        return x
    else:
        x = 100
        return x

if __name__=="__main__":
    main()