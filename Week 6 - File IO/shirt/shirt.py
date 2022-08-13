import sys
import os
from PIL import Image, ImageOps


#bunch of error checking
if len(sys.argv) > 3:
    sys.exit('Too many command-line arguments')
elif len(sys.argv) < 3:
    sys.exit('Too few command-line arguments')
else:
    in_path = sys.argv[1]
    out_path = sys.argv[2]

valid_files = ['.jpg','.jpeg','.png']

if os.path.splitext(in_path)[1] not in valid_files:
    sys.exit('Invalid input')

if os.path.splitext(out_path)[1] not in valid_files:
    sys.exit('Invalid output')

if not os.path.splitext(out_path)[1] == os.path.splitext(in_path)[1]:
    sys.exit('Input and output have different extensions')

try:
    #open the original image
    firstimage = Image.open(in_path)
except FileNotFoundError:
    sys.exit('input does not exist')

#resize shirt to fit image
shirt = Image.open('shirt.png')
size = shirt.size
secondimage = ImageOps.fit(firstimage, size)
#paste new shirt on first image
secondimage.paste(shirt, shirt)
# save output to specified file
secondimage.save(out_path)
