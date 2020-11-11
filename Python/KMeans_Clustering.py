import numpy as np
from scipy.io import loadmat
from scipy.stats import multivariate_normal as norm
import matplotlib.pyplot as plt
from sklearn.mixture import GaussianMixture as GMM
import cv2
import scipy as SP


def main():
    img = cv2.imread('Bottles_small.hdr', -1)
    img = intensity(img)
    cv2.imshow("Did it work?", img)
    cv2.waitKey(0)
    # mean = kmeans(img, 16, 100)
    mean = importanceSampling(img)
    print(mean)


def intensity(img):

    for pixel in img:
        0.2125 * pixel[2] + 0.7154 * pixel[1] + 0.0721 * pixel[0]
    return img[:, :, 0]


def importanceSampling (img):
    mean = np.mean(img, axis=0)
    std = np.std(img, axis=0)

    likeli = SP.stats.norm.pdf(img, mean, std)
    example = randdist(img, likeli, 1)
    print(example)


def randdist(x, pdf, nvals):
    """Produce nvals random samples from pdf(x), assuming constant spacing in x."""

    # get cumulative distribution from 0 to 1
    cumpdf = np.cumsum(pdf)
    cumpdf *= 1/cumpdf[-1]

    # input random values
    randv = np.random.uniform(size=nvals)

    # find where random values would go
    idx1 = np.searchsorted(cumpdf, randv)
    # get previous value, avoiding division by zero below
    idx0 = np.where(idx1==0, 0, idx1-1)
    idx1[idx0==0] = 1

    # do linear interpolation in x
    frac1 = (randv - cumpdf[idx0]) / (cumpdf[idx1] - cumpdf[idx0])
    randdist = x[idx0]*(1-frac1) + x[idx1]*frac1

    return randdist


def kmeans(x, k, n_iter=100):
    '''
    Simple k-means method for computing means from k clusters.

    Parameters
    ----------
    x : numpy.ndarray
        Data points from your training set.
    k : int
        number of clusters.
    n_iter : int, optional
        Number of iterations. The default is 100.

    Returns
    -------
    mean : numpy.ndarray
        Mean values for each k-clusters.
    '''
    # Pick k random points as initial values
    mean = np.random.choice(len(x), size=k, replace=False)
    x, y = np.unravel_index(mean, k)

    # Repeat:
    for _ in range(n_iter):
        # Compute the distance to the mean of each cluster
        dis = np.linalg.norm(x[:, None] - mean, axis=-1)
        # Predict labels
        pred_lbl = np.argmax(dis, axis=-1)

        # Update the cluster mean values from the new labels.
        for i in range(len(mean)):
            mean[i] = np.mean(x[pred_lbl == i], axis=0)

    return mean


main()