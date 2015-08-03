#!/usr/bin/python3
import urllib.request
import os

pages = 93
url = 'http://image.slidesharecdn.com/2-150728061037-lva1-app6892/95/-%d-638.jpg'
filename = 'jpgs/%d_638.jpg'

print(' %d pages downloading...' % pages)

for i in range(1, pages):
    urllib.request.urlretrieve(url % i, filename % i)
    print('page %d succeed.' % i)

#convert jpg to pdf use imagemagick
os.system('convert ./jpgs/*jpg slides.pdf')
