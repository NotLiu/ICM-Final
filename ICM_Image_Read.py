import os,sys
from PIL import Image
from operator import add
from pylab import *
import librosa             # The librosa library
import librosa.display     # librosa's display module (for plotting features)
import IPython.display     # IPython's display module (for in-line audio)
import matplotlib.pyplot as plt # matplotlib plotting functions
import matplotlib.style as ms   # plotting style
import numpy as np
import random


img = Image.open('Brush.png','r')

pix_val = list(img.getdata())

d = {}

pix_sum = 0
'''
for i in pix_val:
    for j in i:
        if j in d:
            d[j] += 1
        else:
            d[j] = 1
'''

d1 = {'R':{},'G':{},'B':{}}
for i in pix_val: #(1,2,3)
    index = 0
    for j in d1: #(0:(),1:(),2:())
        if i[index] in d1[j]:
            d1[j][i[index]] += 1
        else:
            d1[j][i[index]] = 1
        index += 1

for i in d1:
    for j in d1[i]:
        pix_sum += d1[i][j]

#R,G,B value sums

r_sum = 0
g_sum = 0
b_sum = 0



for i in d1:
    for j in d1[i]:
        if i == 'R':
            r_sum += d1[i][j]*j
        elif i == 'G':
            g_sum += d1[i][j]*j
        elif i == 'B':
            b_sum += d1[i][j]*j


print(pix_val,'\n')

#print(d) #number of each number value among RGB

print('Number of each R value:')
for i in d1:
    print(i,':',d1[i])

print('\nSum of Red values: ')
print(r_sum)

print('\nSum of Green values: ')
print(g_sum)

print('\nSum of Blue values: ')
print(b_sum)

print('\nNumber of Pixels:',pix_sum//3)

def cos_wave(A, f, t, sr):
    return [A * cos(2*pi*f*t) for t in arange(0.,t,1./sr)]

f0 = pix_sum//10000;

yy = []
for i in pix_val:
    if max(i) == i[0]: #biggest value of pixel is Red
        y = cos_wave(random.random(), i[0], random.random(), f0)
    if max(i) == i[1]:  # biggest value of pixel is Blue
        y = cos_wave(random.random(), i[1], random.random(), f0)
    if max(i) == i[2]:  # biggest value of pixel is Green
        y = cos_wave(random.random(), i[2], random.random(), f0)
    yy = yy + y

IPython.display.Audio(data=yy, rate=4410)