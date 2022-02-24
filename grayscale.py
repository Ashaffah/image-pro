from os.path import isfile, join
import cv2

import os,glob

from os import listdir,makedirs

from os.path import isfile,join
path = 'C:\\Users\\Morph_k\\Desktop\\Pak Tri\\Original\\Bebek' # Asal Folder 
dstpath = 'C:\\Users\\Morph_k\\Desktop\\Pak Tri\\GrayScale\\Bebek' # Destinasi Folder
try:
    makedirs(dstpath)
except:
    print ("Directory sudah ada, gambar akan di render di folder yang sama")
# Folder tidak terpakai
files = [f for f in listdir(path) if isfile(join(path,f))] 
for image in files:
    try:
        img = cv2.imread(os.path.join(path,image))
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        dstPath = join(dstpath,image)
        cv2.imwrite(dstPath,gray)
    except:
        print ("{} tidak terkonversi".format(image))
for fil in glob.glob("*.jpg"):
    try:
        image = cv2.imread(fil) 
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # Konversi ke greyscale
        cv2.imwrite(os.path.join(dstpath,fil),gray_image)
    except:
        print('{} tidak terkonversi')

path = 'C:\\Users\\Morph_k\\Desktop\\Pak Tri\\Original\\Ayam'  # Asal Folder
dstpath = 'C:\\Users\\Morph_k\\Desktop\\Pak Tri\\GrayScale\\Ayam'  # Destinasi Folder
try:
    makedirs(dstpath)
except:
    print("Directory sudah ada, gambar akan di render di folder yang sama")
# Folder tidak terpakai
files = [f for f in listdir(path) if isfile(join(path, f))]
for image in files:
    try:
        img = cv2.imread(os.path.join(path, image))
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        dstPath = join(dstpath, image)
        cv2.imwrite(dstPath, gray)
    except:
        print("{} tidak terkonversi".format(image))
for fil in glob.glob("*.jpg"):
    try:
        image = cv2.imread(fil)
        # Konversi ke greyscale
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        cv2.imwrite(os.path.join(dstpath, fil), gray_image)
    except:
        print('{} tidak terkonversi')
