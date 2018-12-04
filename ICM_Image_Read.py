import os,sys
from PIL import Image

img = Image.open('Andrew.jpg','r')

pix_val = list(img.getdata())

d = {}

pix_sum = 0

for i in pix_val:
    for j in i:
        if j in d:
            d[j] += 1
        else:
            d[j] = 1

for i in d:
    pix_sum += d[i]

print(pix_val)
print(d)
print('sum:',pix_sum/3)