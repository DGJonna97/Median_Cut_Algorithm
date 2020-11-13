import random

import cv2
import numpy as np
from collections import namedtuple
from scipy.stats import multivariate_normal as norm

import scipy

def Create1DDistribution(values):
    mean = np.mean(values, axis=0)
    std = np.std(values, axis=0)
    sumPDF = np.sum(scipy.stats.norm.pdf(values, mean, std))

    if sumPDF <= 0:
        PDF =  np.zeros((np.shape(values)))
        sumPDF = 1.0
    else:
        PDF = values

    CDF = np.cumsum(PDF)
    maxCDF = np.max(CDF)

    if maxCDF > 0:
        CDF = CDF / maxCDF



    distr = namedtuple("distr", "pdf cdf maxcdf")
    out = distr(pdf= PDF / sumPDF, cdf=CDF, maxcdf=maxCDF)
    return out

def Sampling1DDistribution(distr,u):

    val = np.argmin (np.abs(distr.cdf - u))
    pdf = distr.pdf[val]
    return val, pdf

def polarvector(theta, phi):
    sinTheta = np.sin(theta)
    vec = [np.cos(phi) * sinTheta, np.cos(theta), np.sin(phi) * sinTheta]
    return vec

def importanceSampling(img, nSamples):

    r,c = np.shape(img)
    cDistr= []
    values = np.zeros((c,1))

    for i in range (0,c):
        tmpDistr = Create1DDistribution(img[:, i])
        cDistr.append( tmpDistr)

        values[i] = tmpDistr.maxcdf # maxCDF

    rDistr = Create1DDistribution(values)

    samples = []
    imgOut = cv2.imread('Bottles_Small.hdr', -1)
   # imgOut = np.zeros(np.shape(img))
    pi22 = 2 * np.pi ** 2

    for i in range (1,nSamples):
        x, pdf1 = Sampling1DDistribution(rDistr,random.random())

        y, pdf2 = Sampling1DDistribution(cDistr[x], random.random())
       # angles = np.pi *[2 * x / c, y / r]
       # vec = polarvector(angles[1], angles[0])
       # pdf = (pdf1 * pdf2) / (pi22 * abs(np.sin(angles[0])))
        # creating a sample

        sample = 'x', x / c, 'y', y / r, 'col', img[y, x]
        samples.append(sample)

        imgOut[y, x] +=  [0,0,255]
    return imgOut, samples


#img = cv2.imread('Bottles_Small.hdr', -1)  # reads BGR image
#intensityMap, ogimg = intensity(img)  # returns 2d array of intensity values and the greyscaled image
#img, samples = importanceSampling(intensityMap,1024)
#cv2.imshow("imgout", img)
#cv2.waitKey(0)
