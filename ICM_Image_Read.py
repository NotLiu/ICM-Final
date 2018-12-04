import os,sys
from PIL import Image

img = Image.open('Tiara.png','r')

pix_val = list(img.getdata())

print(pix_val)