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
    
    fig, ax = plt.subplots()
    ax.imshow(testImage[0])
    ax.scatter(predictionResults[0,:16]*255.0,predictionResults[0,16:32]*255.0, c = '#ff7f0e')
    
    return predictionResults 