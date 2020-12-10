import numpy as np
from scipy.io import loadmat
from scipy.stats import multivariate_normal as norm
import matplotlib.pyplot as plt
from sklearn.mixture import GaussianMixture as GMM

def color(img, x,y):
    r,g,b = [],[],[]
    for i in x:
        b,g,r = img[x[i],y[i]]
    return r,g,b

