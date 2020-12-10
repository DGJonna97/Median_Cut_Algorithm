# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 09:42:05 2020

@author: NCJ
"""

from tensorflow import keras
from tensorflow.keras import layers

from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense

import matplotlib.pyplot as plt
from PIL import Image
import os, os.path
import glob
import numpy as np
import cv2
import pandas as pd
from numpy import genfromtxt
import tensorflow as tf



def deep_learning(testImage,numLights): 
        
    model = tf.keras.models.load_model('Deep_Learning_Model')
    
    predictionResults = model.predict(testImage[:1])
    
    #fig, ax = plt.subplots()
    #ax.imshow(testImage[0])
    #ax.scatter(predictionResults[0,:16]*255.0,predictionResults[0,16:32]*255.0, c = '#ff7f0e')
    #plt.show()
    predictionResults = predictionResults*255
    data_set = {"centerx": predictionResults[0,0:16], "centery": predictionResults[0,16:32]}
    return data_set


#img = cv2.imread('cheese.jpg', -1)
#img2 = np.copy(img/255)
#resized = cv2.resize(img2, (256,256), interpolation = cv2.INTER_AREA)

#img4D = np.empty((1, 256, 256, 3), dtype='uint8')

#img4D[0, :, :, :] = resized

#dataset = deep_learning(img4D, 32)


#x = dataset["centerx"]
#y = dataset["centery"]

#for i in range(0,len(x)):
#    cv2.circle(resized, (int(x[i]), int(y[i])), 5, (0, 255, 0), -1)


#cv2.imshow("re", resized)
#cv2.waitKey(0)
#print(dataset)