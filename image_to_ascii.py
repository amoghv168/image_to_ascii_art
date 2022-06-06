# A Python project to convert an HD image into ascii art

from PIL import Image
import numpy as np

def avg_brightness(tile):
    t = np.array(tile)
    w, h = np.shape(t)
    return np.average(np.reshape(t, w*h))

grayscale_ascii = r"$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~i!lI;:,\"^`'. "

filename = r"C:\Users\Amogh\Downloads\photo-1597871040916-4b4c20ba08dd.jpg"

img = Image.open(filename).convert('L')

width, height = img.size[0], img.size[1]

columns = 250

tile_width = width / columns
tile_height = tile_width / 0.43

rows = int(height / tile_height)

ascii_rows = []

for row in range(rows):
    y1 = int(row * tile_height)
    y2 = int((row * tile_height) + tile_height)
    if row == rows - 1:
        y2 = height # End correction
    ascii_rows.append("")
    for column in range(columns):
        x1 = int(column * tile_width)
        x2 = int((column * tile_width) + tile_width)
        if column == columns - 1:
            x2 = width # End correction
            
        tile = img.crop((x1, y1, x2, y2))
        avg_b = avg_brightness(tile)  
        ascii_rows[row] += grayscale_ascii[int((avg_b * 68.999) / 255)]

f = open(r"C:\Users\Amogh\Desktop\Python Experiments\image_to_ascii\image_to_ascii.txt", 'w')
for a_row in ascii_rows:
    f.write(a_row + '\n')
f.close()
            
        


















