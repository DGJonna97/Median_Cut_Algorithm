# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 13:57:18 2020

@author: NCJ
"""

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.datasets.samples_generator import make_blobs
from sklearn.cluster import KMeans

import struct
import cv2

def intensity(img):
    # loop trough every pixel and modify the color values, before adding them together into intensity
    print("Greyscaling...")
    width = int(img.shape[1])
    height = int(img.shape[0])
    tempvalues = []
    greyimg = img # local var to show greyscaled pic
    for i in range(0, height):
        row = []
        for j in range(0, width):
            pixel = img[i, j]
            pixelIntensity = 0.2125*pixel[2] + 0.7154*pixel[1] + 0.0721*pixel[0]  # BGR image
            greyimg[i, j] = pixelIntensity
            row.append(pixelIntensity)
        tempvalues.append(row)
    print("OG img shape " + str( np.shape(img)))
    print("intensity values shape " + str(np.shape(tempvalues)))

    return tempvalues, greyimg # returns 2d array of intensity values and the greyscaled img




img = cv2.imread('Grace.jpg', cv2.IMREAD_COLOR) # reads BGR image
intensity, grey = intensity(img) # returns 2d array of intensity values and the greyscaled image

#cv2.imshow("Grace", grey)
#cv2.waitKey(0)

grey2D = grey[:,:]

kmeans = KMeans(n_clusters=64, init='k-means++', max_iter=600, n_init=10, random_state=0)

pred_y = kmeans.fit_predict(intensity)

plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='green')




"""
X, y = make_blobs(n_samples=300, centers=5, cluster_std=0.60, random_state=0)
plt.scatter(X[:,0], X[:,1])


wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=0)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)
plt.plot(range(1, 11), wcss)
plt.title('Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()


kmeans = KMeans(n_clusters=5, init='k-means++', max_iter=300, n_init=10, random_state=0)
pred_y = kmeans.fit_predict(X)
plt.scatter(X[:,0], X[:,1])
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='green')
plt.show()
"""
