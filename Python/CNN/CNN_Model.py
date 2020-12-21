# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 11:13:31 2020

@author: NCJ
"""
# include all packages etc.

from tensorflow.keras.datasets import cifar10 
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
from tensorflow.keras.datasets import cifar10 
from tensorflow import keras
from tensorflow.keras import layers
from keras import backend as K
import random

from DeepLearningPython import deep_learning


img = plt.imread("samepics/training/0.jpg")

#plt.imshow(img)

# Get training labels, output points from kmenans method
points = genfromtxt('samepics/results.csv', delimiter=';')

x  = points[0:len(points)-1,0]
y = points[0:len(points)-1,1]


# Define number of training images and number of lights to place
numSamples = 2100
numLights = 16

# Define arrays for images
x_train = np.empty((numSamples, 256, 256, 3), dtype='uint8')
x_test = np.empty((3, 256, 256, 3), dtype='uint8')


testImg = cv2.imread('samepics/test/testy0.jpg',-1)


# Load church test image
graceImg = cv2.imread('Grace.jpg',-1)

graceImg = cv2.resize(graceImg, dsize=(256, 256), interpolation=cv2.INTER_CUBIC)

#plt.imshow(graceImg)


# make load images function

def load_images_from_folder(folder):


    images = []
    folder2 = os.listdir(folder)
    for i in range(0,len(folder2)):
        filename = folder2[i]
        img = cv2.imread(os.path.join(folder,filename))
        if img is not None:
            images.append(img)
            #print(os.path.dirname(os.path.dirname(folder)))
            
        #shutil.move((folder+"/"+str(i)+".jpg"), "C:/Users/tobia/Desktop/Images/tranning")
    return images


images = load_images_from_folder('samepics/training/') # Choose folder with 256*256 images


# Images into image array
for i in range(1,numSamples-1):
    
    x_train[i, :, :, :] = images[i]
    
    
    
#----------------Test images get

instances = []
a = 0

for filepath in os.listdir('samepics/test/'):
    instances.append(cv2.imread('samepics/test/{0}'.format(filepath),-1))

for i in range(1,3-1):
    
    x_test[i, :, :, :] = instances[i]
   


#cheeseImg = cv2.imread('cheese.jpg',cv2.IMREAD_COLOR)
cheeseImg = cv2.imread('cheese.jpg',-1)



img2 = np.copy(cheeseImg)
resized = cv2.resize(img2, (256,256), interpolation = cv2.INTER_AREA)


x_test[0, :, :, :] = resized

# Normalize images

x_train = x_train/255.0


x_test = x_test/255.0



# Divide labels into groups of 16
def divide_chunks(l, n): 

    for i in range(0, len(l), n):  
            yield l[i:i + n] 


x = list(divide_chunks(x,numLights))
y = list(divide_chunks(y,numLights))
x = x[0:numSamples]
y = y[0:numSamples]


arrayX = np.array(x)
arrayY = np.array(y)


arrayXY = np.zeros((numSamples,numLights*2))


arrayXY[:,0:numLights] = arrayX

arrayXY[:,numLights:numLights*2] = arrayY

arrayXY = arrayXY/255.0


# Build model

model = Sequential()
model.add(Conv2D(32, (3,3), input_shape=(256, 256, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2), padding = 'same'))

model.add(Conv2D(64, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(128, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())
model.add(Dense(64))
model.add(Activation('relu'))

model.add(Dropout(0.5))
model.add(Dense(32))
model.add(Activation('sigmoid'))

# compile model
model.compile(loss = 'MeanAbsoluteError',
              optimizer = 'Adam',
              metrics = ['MeanAbsoluteError'])


# train model, input is train images, labels are kmeans light centroids, 16 points per image
model.fit(x_train,arrayXY,epochs=3)



# Save model, can be loaded by 
results = model.save('Deep_Learning_Model_16')


predictionResults = deep_learning(x_test[:2],numLights)


#plt.scatter(predictionResults[0,:16],predictionResults[0,16:32])






