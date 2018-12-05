import os,sys
from PIL import Image

img = Image.open('Andrew.jpg','r')

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
    for j in i:
        pix_sum += 1

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


print('All pixel RGB data:\n')
print(pix_val,'\n')

#print(d) #number of each number value among RGB

print('Number of each R value:')
for i in d1:
    print(i,':',d1[i])

print('Sum of Red values: ')
print(r_sum)

print('Sum of Green values: ')
print(g_sum)

print('Sum of Blue values: ')
print(b_sum)

print('Number of Pixels:',pix_sum//3)