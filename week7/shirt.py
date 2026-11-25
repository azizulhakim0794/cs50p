# python3 shirt.py before1.jpg after.jpg 

import sys
from PIL import Image,ImageOps

if len(sys.argv) < 3:
    print("Too few command-line arguments")
    sys.exit(1)

if len(sys.argv) > 3 :
    print("Too many command-line arguments")
    sys.exit(1)

read_file = sys.argv[1]
write_file = sys.argv[2]

# read_file = "before1.jpg"
# write_file = "after.jpg"

# filename = "image.profile.jpg"

read_file_extension = read_file.split(".")[-1]
write_file_extension = write_file.split(".")[-1]

ex_list =  ["jpg", "png","jpeg"]

if read_file_extension not in ex_list or write_file_extension not in ex_list:
    print("Invalid input")
    sys.exit(1)

if read_file_extension != write_file_extension and read_file.endswith((".jpg", ".png","jpeg")):
    print("Input and output have different extensions")
    sys.exit(1)


try:
    shirt = Image.open("shirt.png")
    size = shirt.size
    with Image.open(read_file) as im:
        resize_image = ImageOps.fit(im, size)

        resize_image.paste(shirt, (0, 0), shirt)
        resize_image.save(write_file)

    shirt.close()

except FileNotFoundError:
    print("Input does not exist")
    sys.exit(1)