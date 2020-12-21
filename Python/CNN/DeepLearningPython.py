# -*- coding: utf-8 -*-
"""
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
    
    if numLights == 16 :   
        model = tf.keras.models.load_model('Deep_Learning_Model_16')
    elif numLights == 32 :  
        model = tf.keras.models.load_model('Deep_Learning_Model_32')

    
    predictionResults = model.predict(testImage[:1])
    
    fig, ax = plt.subplots()
    ax.imshow(testImage[0])
    ax.scatter(predictionResults[0,:numLights]*255.0,predictionResults[0,numLights:numLights*2]*255.0, c = '#ff7f0e')
    
    return predictionResults 



