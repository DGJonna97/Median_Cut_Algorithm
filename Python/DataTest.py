# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 11:13:31 2020

@author: NCJ
"""

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


(t,y_train),(y,u)=cifar10.load_data()


img = plt.imread("samepics/training/0.jpg")

#plt.imshow(img)

points = genfromtxt('samepics/results.csv', delimiter=';')

x  = points[0:len(points)-1,0]
y = points[0:len(points)-1,1]

numSamples = 2100

x_train = np.empty((numSamples, 256, 256, 3), dtype='uint8')
x_test = np.empty((3, 256, 256, 3), dtype='uint8')


testImg = cv2.imread('samepics/test/testy0.jpg',cv2.IMREAD_COLOR)




testPoints = genfromtxt('samepics/resultstest.csv', delimiter=';')

testX  = testPoints[0:len(testPoints)-1,0]
testY = testPoints[0:len(testPoints)-1,1]



#plt.imshow(testImg)


#----------------train images get
instances = []
a = 0
# Load in the images
for filepath in os.listdir('samepics/training/'):
    instances.append(cv2.imread('samepics/training/{0}'.format(filepath),cv2.IMREAD_COLOR))

for i in range(1,numSamples-1):
    
    x_train[i, :, :, :] = instances[i]
    a += 1
    
    
#----------------Test images get

instances = []
a = 0

for filepath in os.listdir('samepics/test/'):
    instances.append(cv2.imread('samepics/test/{0}'.format(filepath),cv2.IMREAD_COLOR))

for i in range(1,3-1):
    
    x_test[i, :, :, :] = instances[i]
    a += 1



#x_train = x_train/255.0
x_train = x_train/255.0

#x_test = x_test/255.0
x_test = x_test/255.0


y_train = y_train[0:numSamples]



def divide_chunks(l, n): 

    for i in range(0, len(l), n):  
            yield l[i:i + n] 



x = list(divide_chunks(x,16))
y = list(divide_chunks(y,16))
x = x[0:numSamples]
y = y[0:numSamples]

testX = list(divide_chunks(testX,16))
testY = list(divide_chunks(testY,16))

testX = testX[0:500]
testY = testY[0:500]

testX = np.array(testX)
testY = np.array(testY)

arrayX = np.array(x)
arrayY = np.array(y)

testXY = np.zeros((500,32))

arrayXY = np.zeros((numSamples,32))

testXY[:,0:16] = testX

testXY[:,16:32] = testY

arrayXY[:,0:16] = arrayX

arrayXY[:,16:32] = arrayY

arrayXY = arrayXY/255.0

testXY = testXY/255.0


#cv2.imshow('image',x_train[0])




model = Sequential()
model.add(Conv2D(32, (3, 3), input_shape=(256, 256, 3)))
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

model.compile(loss = 'MeanSquaredError',
              optimizer = 'Adam',
              metrics = ['MeanSquaredError'])

model.fit(x_train,arrayXY,epochs=20)


predictionResults = model.predict(x_test[:2])

#plt.scatter(testXY[0,:16],testXY[0,16:32])

#plt.scatter(predictionResults[0,:16],predictionResults[0,16:32])
#transpose convolution    One hot
 
fig, ax = plt.subplots()
ax.imshow(x_test[1])
ax.scatter(testXY[1,:16]*255.0,testXY[1,16:32]*255.0)
ax.scatter(predictionResults[1,:16]*255.0,predictionResults[1,16:32]*255.0)