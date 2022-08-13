var = input('what is your variable name in camelcase? ').strip()

for c in var:
    if c.isupper():
        c = c.lower()
        print('_', sep="", end="")
    print(c, sep="", end ="")
print()