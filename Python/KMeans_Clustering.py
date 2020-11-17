import numpy as np
import matplotlib.pyplot as plt
import cv2
import ImportanceSampling
from sklearn.cluster import KMeans
import time


def intensity(img):
    """
    Method for finding the intensity values of the input image

    Parameters
    ----------
    img: 3D array from cv2
        The image to find intensity values within
    Returns
    -------
    _ : 2D array of floats
        The found intensities of all the pixels in img
    """
    for pixel in img:
        0.2125 * pixel[2] + 0.7154 * pixel[1] + 0.0721 * pixel[0]
    return img[:, :, 0]


def findcolor(label):
    """
    Method for matcihng a label with a corresponding color

    Parameters
    ----------
    label: int
        A label for a specefic sample

    Returns
    -------
    _ : String
        Color string that fits the input label
    """
    return {
        0: 'blue',
        1: 'maroon',
        2: 'green',
        3: 'orange',
        4: 'steelblue',
        5: 'violet',
        6: 'grey',
        7: 'magenta',
        8: 'darkgreen',
        9: 'khaki',
        10: 'powderblue',
        11: 'indigo',
        12: 'fuchsia',
        13: 'purple',
        14: 'navajowhite',
        15: 'gold',
        16: 'azure',
        17: 'plum',
        18: 'darkorange',
        19: 'bisque',
        20: 'crimson',
        21: 'pink',
        22: 'peru',
        23: 'brown',
        24: 'wheat',
        25: 'aliceblue',
        26: 'seashell',
        27: 'gainsboro',
        28: 'mintcream',
        29: 'palegreen',
        30: 'rosybrown',
        31: 'hotpink',
    }.get(label, 0)


def plotresults(labels, samples, kmeans, img):
    """
    Method for plotting the results of the kmeans

    Parameters
    ----------
    labels : list of ints
        List of the resulting labels found for each sample
    samples : 2D array of ints
        (x,y) postions of the samples pixels
    kmeans : Object
        resulting from the kmeans.fit() method
    img : 3D array from cv2
        original image put into main()

    Returns
    -------
    imgOut2 : 3D array of ints
        Copy of img but with drawn clusters on top
    """
    plt.figure("Kmeans clustering", figsize=(10,8))
    plt.clf()
    plt.grid(True)
    plt.xticks(())
    plt.yticks(())
    plt.gca().invert_yaxis()
    plt.suptitle( "Kmeans clustering, " + str(len(samples.T)) + " Samples, " + str(len(kmeans.cluster_centers_)) + " clusters", fontsize=16)

    samples = samples.T

    #imgOut = np.zeros(np.shape(img))
    imgOut2 = np.copy(img)
    for i in range(0, len(labels)):
        samx, samy = samples[i]
        color = findcolor(labels[i])
        plt.scatter(samx, samy, c=color, s=5, label=color, alpha=1, edgecolors='none')

    #ax.legend()

    centroids = kmeans.cluster_centers_
    plt.scatter(centroids[:, 0], centroids[:, 1],
                marker='x', s=20, linewidths=3,
                color='r', zorder=10)
    # cv2.imshow("imgout", imgout)
    #ax.view_init(30, 90)

    for cen in centroids:
        cv2.circle(imgOut2, (int(cen[0]), int(cen[1])), 5, (0, 255, 0), -1)

    return imgOut2


def intensitymetric(intensitymap, samples):
    """
    Method for matching a sample with the corresponding intensity

    Parameters
    ----------
    intensitymap : 2D array of floats
        Consists of intensity values
    samples : 2D array of ints
        (x,y) postions of the samples pixels

    Returns
    -------
    lums : list
        Intensity values for the samples
    """

    lums = []
    for i in range(0, len(samples.T)):
        value = intensitymap[samples[1][i], samples[0][i]]
        lums.append(value)
    return lums


def main(img, nSamples, nLightSources, weights=False):
    """
    k-means method for computing light sources position from clusters.

    Parameters
    ----------
    img : 3D array of ints from cv2
        The image to find light sources in.
    nSamples : int
        How many samples to take from the input picture.
    nLightSources : int
        Number of lightsources, which will be the number of clusters.
    weights :  bool, default false
        whether the calculation should take the weight of the samples into account.
    """
    start_time = time.time()

    intensitydata = intensity(img)
    samplepic, samples = ImportanceSampling.importanceSampling(intensitydata, nSamples)

    intmetric = intensitymetric(intensitydata, samples)

    kmeans = KMeans(n_clusters=nLightSources, random_state=0, ).fit(samples.T)

    pictitle=""
    if weights:
        pictitle= " with weights"
        w = intmetric / np.max(intmetric)
        labels = kmeans.predict(samples.T, w)
    else:
        pictitle = " without weights"
        labels = kmeans.predict(samples.T)

    print("done with kmeans in  --- %s seconds ---" % (time.time() - start_time))

    result = plotresults(labels, samples, kmeans, img)
    print("done with plotting in  --- %s seconds ---" % (time.time() - start_time))

    cv2.imshow("original pic", img)
    cv2.imshow("samples pic" + pictitle, samplepic)
    cv2.imshow("Clusters on original pic" + pictitle, result)
    plt.show()
    cv2.waitKey(0)


img = cv2.imread('Bottles_Small.hdr', -1)
main(img, 1024, 32, True)
