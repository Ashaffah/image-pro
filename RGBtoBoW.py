from skimage import io, color
import os
import imghdr

source = r'C:\Users\user\Desktop\Pak Tri\Original\Bebek'
destination = r'C:\Users\user\Desktop\Pak Tri\BoW\Bebek'

image_files = [os.path.join(root, filename) 
                   for root, dirs, files in os.walk(source) 
                   for filename in files 
                   if imghdr.what(os.path.join(root, filename))]

for fn in image_files:
    rgb = io.imread(fn)
    grey = color.rgb2gray(rgb)
    head, tail = os.path.split(fn)
    io.imsave(os.path.join(destination, tail), grey)
