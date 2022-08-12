#phrase = input('enter your equation: ').strip().split()
#x = phrase[0]
#y = phrase[1]
#z = phrase[2]
x, y, z = input('enter your equation: ').strip().split()
x = int(x)
z = int(z)

if int(x):
    if int(z):
        if y == '+':
            ans = float(x + z)

        if y == '-':
            ans = float(x - z)
        if y == '*':
            ans = float(x*z)
        if y == '/' and z != 0:
            ans = float (x /z)
print(f"{ans:.1f}")