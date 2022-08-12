import sys

#error checking for proper input
if len(sys.argv)==2:
    filename = sys.argv[1]
elif len(sys.argv) > 2:
    sys.exit('Too many command-line arguments')
else:
    sys.exit('Too few command-line arguments')

#checking proper file
if not filename.endswith('.py'):
    sys.exit('Not a Python file')

try:
    file = open(filename)
    lines = file.readlines()
    count = 0
    for line in lines:
        if line.lstrip().startswith('#'):
            # dont count comments
            continue
        elif line.isspace():
            # don't count empty lines
            continue

        else:
            count += 1
    file.close()
    print(count)
except FileNotFoundError:
    sys.exit('File does not exist')