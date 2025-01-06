from wand.image import Image
from wand.color import Color
import glob
import math
import random


# Generate transparent png as a blank space
# with Image(width = 1500, height = 1500) as img:
#     img.save(filename ='assets/transparent.png')


# Duplicate icons to fill grid
cols = 13 # odd
rows = 6 # even
dim = [cols, rows]
assets = glob.glob("assets/*/*.png")
# Get at minimum the number of icons to fill grid
icons = assets * math.ceil(cols*rows / len(assets))
# Truncate excess icons
icons = icons[:math.floor(cols*rows / 2)]

# shuffle icons
random.shuffle(icons)


# Insert blanks spaces, +1 stagger to have icon in upper left
for i in range(len(icons)):
    # Add blank space every other icon, +1 to have icon in upper right
    icons.insert(i*2 + 1, "assets/transparent.png")


# Match first and last column to wrap background
for r in range(rows):
    icons[r*cols + cols - 1] = icons[r*cols]


# Arrange icons in a grid and transform (rotate, pad, resize)
with Image() as img:
    for icon in icons:
        with Image(width=64, height=64, pseudo=icon) as item:
            item.rotate(-6) # degrees
            img.image_add(item)
    img.background_color = "#b2b2b2"
    img.montage(thumbnail = "25x25%^ + 150+150", tile = "{0}x{1}".format(*dim))
    img.save(filename = "output/grid.png")