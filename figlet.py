import sys
import random
from pyfiglet import Figlet


figlet = Figlet()
fonts = figlet.getFonts()

if len(sys.argv) == 1:
    #pick a random font
    font = random.choice(fonts)
elif len(sys.argv)==3:
    # user chose a specific font
    if not (sys.argv[1] == '-f' or sys.argv[1]=='--font'):
        print('Invalid usage')
        sys.exit(1)
    if sys.argv[2] not in fonts:
        print('Invalid usage')
        sys.exit(1)
    figlet.setFont(font=sys.argv[2])
else:
    print('Invalid usage')
    sys.exit(1)


#prompt user for text
text = input('enter your text: ').strip()

#outputs text in desired font
print(figlet.renderText(text))