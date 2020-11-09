# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 13:12:36 2020

@author: KAFF
"""
import statistics
import cv2
import numpy as np
import math

img2 = cv2.imread('Bottles_Small.hdr', -1)

tonemapReinhard = cv2.createTonemapReinhard()
ldrReinhard = tonemapReinhard.process(img2)

img = np.clip(ldrReinhard * 255, 0, 255).astype('uint8')

cv2.imshow("0", img)
cv2.waitKey(0)

xMin = 0
xMax = 300
yMax = 300
yMin = 0

pic = img[xMin:xMax, yMin:yMax]

r = pic[:,:,2]
g = pic[:,:,1]
b = pic[:,:,0]

avg_r = np.average(r)/255.0
avg_g = np.average(g)/255.0
avg_b = np.average(b)/255.0

img_value = np.max(img)

cv2.circle(img2, (50, 50), 50, (avg_b, avg_g, avg_r), -1)
cv2.circle(img2, (50, 50), 5, (0, 255, 0), 1)

cv2.imshow("1", img2)
cv2.waitKey(0)
