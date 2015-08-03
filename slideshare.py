#!/usr/bin/python3
import urllib.request
import os

pages = 93
url = 'http://image.slidesharecdn.com/xxxxxxxxxxxxxxxxxxxxxxxxxxx/xx/-%d-xxx.jpg'
filename = 'jpgs/%d_xxx.jpg'

print(' %d pages downloading...' % pages)

os.system('mkdir ./jpgs/')

for i in range(1, pages):
    urllib.request.urlretrieve(url % i, filename % i)
    print('page %d succeed.' % i)

#convert jpg to pdf use imagemagick
os.system('convert ./jpgs/*jpg slides.pdf')
