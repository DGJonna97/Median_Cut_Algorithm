import random
import cv2
import numpy as np
from collections import namedtuple
from scipy.stats import multivariate_normal as norm
import scipy

def positionMetric(sample, mean):
    # u and v are the unit vectors representing the positions of the samples u and v
    dot = np.dot(mean,sample)
    mag = np.linalg.norm(sample)*np.linalg.norm(mean)
    magnitude = np.sqrt(np.power(mean[0],2 )+ np.power(mean[1],2 ) ) *  np.sqrt(np.power(sample[0], 2) + np.power(sample[1], 2))

    angle = np.arccos(dot/magnitude)/np.pi


    return angle


def luminanceMetric(intensitymap, samples, mean):
    #The luminance metric can be defined by the difference in the
    #luminance between two samples. This can then be limited to
    #the range [0,1] by normalising
    lumu  = intensitymap[mean[0], mean[1]]
    lumv = intensitymap[samples[0], samples[1]]
    lum = np.abs(lumu-lumv)/np.max(intensitymap)
    return lum

def main(intensitymap, samples, mean ):
    pos = positionMetric(samples, mean)
    lum = luminanceMetric(intensitymap, samples, mean)
    distancemeasure = pos+lum
    return distancemeasure
#mean = [1,0]
#sample = [2,1]
#intensitymap= np.array([[255,255,254], [0, 20, 30], [254,10,5]], np.int32)
#
#print(pos)
#
#print(lum)
#
#print(distancemeasure*3)