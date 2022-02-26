# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 00:15:15 2020

@author: Ashaffah
"""

import cv2
import numpy as np

img = cv2.imread('Meew.jpg') #image source
retval, threshold = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY)
grayscaled = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
retval, threshold1 = cv2.threshold(grayscaled, 10, 255, cv2.THRESH_BINARY)
retval2,threshold2 = cv2.threshold(grayscaled,125,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
thres = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)

resize_img = cv2.resize(img, (200,200), interpolation = cv2.INTER_AREA)
resize_img1 = cv2.resize(threshold, (200,200), interpolation = cv2.INTER_AREA)
resize_img2 = cv2.resize(grayscaled, (200,200), interpolation = cv2.INTER_AREA)
resize_img3 = cv2.resize(threshold1, (200,200), interpolation = cv2.INTER_AREA)
resize_img4 = cv2.resize(threshold2, (200,200), interpolation = cv2.INTER_AREA)

cv2.imshow('original', resize_img)
cv2.imshow('threshold', resize_img1)
cv2.imshow('grayscaled', resize_img2)
cv2.imshow('otsu', resize_img3)
cv2.imshow('adaptive thresholding', resize_img4)
cv2.waitKey(0)
cv2.destroyAllWindows()
