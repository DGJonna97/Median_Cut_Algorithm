from asyncio import wait
import time

import numpy as np
from scipy.io import loadmat
from scipy.stats import multivariate_normal as norm
import matplotlib
import matplotlib.pyplot as plt
import threading, queue
import matplotlib.animation as animation

q = queue.Queue()


def switch_demo(label):
    if label == 0:
        return 'blue'
    elif label == 1:
        return 'red'
    elif label == 2:
        return 'green'
    elif label == 3:
        return 'orange'
    elif label == 4:
        return 'steelblue'
    elif label == 5:
        return 'violet'
    elif label == 6:
        return 'grey'
    elif label == 7:
        return 'magenta',
    elif label == 8:
        return 'darkgreen',
    elif label == 9:
        return 'khaki',
    elif label == 10:
        return 'powderblue',
    elif label == 11:
        return 'indigo',
    elif label == 12:
        return 'fuchsia',
    elif label == 13:
        return 'purple',
    elif label == 14:
        return 'navajowhite',
    elif label == 15:
        return 'teal',

class AnimatedScatter(object):




    def plotthatshit(self, labels,samples,kmeans):

        #ax.set_facecolor('black')
        for i in range(0, len(labels)):
            color = switch_demo(labels[i])
            samx = samples[0][i]
            samy =  samples[1][i]
            self.scat = self.ax.scatter(samx, samy, c=color, s=5, label=color,
                       alpha=1, edgecolors='none')

        #ax.legend()
        self.ax.grid(True)

        centroids = kmeans
        self.scat  = self.ax.scatter(centroids[:, 0], centroids[:, 1],
                    marker='x', s=20, linewidths=3,
                    color='r', zorder=10)
        # cv2.imshow("imgout", imgout)

        plt.xticks(())
        plt.yticks(())
        """h = .02
        x_min, x_max = samples[:, 0].min() - 1, samples[:, 0].max() + 1
        y_min, y_max = samples[:, 1].min() - 1, samples[:, 1].max() + 1
        xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    
        # Obtain labels for each point in mesh. Use last trained model.
        Z =  kmeans.predict(np.c_[xx.ravel(), yy.ravel()])
    
        # Put the result into a color plot
        Z = Z.reshape(xx.shape)
        plt.figure(1)
        plt.clf()
        plt.imshow(Z, interpolation='nearest',
                   extent=(xx.min(), xx.max(), yy.min(), yy.max()),
                   cmap=plt.cm.Paired,
                   aspect='auto', origin='lower')
        """
        plt.show()
        return self.scat,

    def update(self):
        """Update the scatter plot."""

        ost2 = q.get()
        labels, inertia, centers, n_iter = ost2[0], ost2[1], ost2[2], ost2[3]
        for i in range(0, len(labels)):
            color = switch_demo(labels[i])
            samx = samples[0][i]
            samy = samples[1][i]
            self.scat.set_offsets(samx, samy, c=color, s=5, label=color,
                            alpha=1, edgecolors='none')

            # ax.legend()


        centroids = kmeans
        self.scat.set_offsets(centroids[:, 0], centroids[:, 1],
                        marker='x', s=20, linewidths=3,
                        color='r', zorder=10)
        # cv2.imshow("imgout", imgout)

        return self.scat,

    def __init__(self, samples):

        self.ani = animation.FuncAnimation(self.fig, self.update, interval=5,
                                           init_func=self.plotthatshit, blit=True)

        self.fig, self.ax = plt.subplots(figsize=(15, 15))
        plotismade= False


        while True:
            time.sleep(15)


            #q.task_done()
            if not plotismade:
                plotthatshit(self,labels,samples,centers)
            else:
                update(self,labels,samples,centers)

            plt.show()

