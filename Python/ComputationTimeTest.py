import kmeans
import os
import cv2
import csv
import shutil
import random
import time
import numpy
import FinalMedianCut
import DeepLearningPython
from prettytable import PrettyTable

def load_images_from_folder(folder, numberofimages):

    #amount = int(len(os.listdir(folder))*0.7)

    images = []
    folder2 = os.listdir(folder)
    random.shuffle(folder2)
    for i in range(0, numberofimages or len(folder2)):
        filename = folder2[i]
        img = cv2.imread(os.path.join(folder,filename),-1)
        if img is not None:
            images.append(img)
            #shutil.copy2(folder+"/"+filename, os.path.dirname(os.path.dirname(folder))+"/"+ str(nLights))

        #shutil.move((folder+"/"+str(i)+".jpg"), "C:/Users/tobia/Desktop/Images/tranning")
    return images

def compute(images,nLights):
    mComtime = []
    kComtime = []
    cComtime = []
    for img in images:
        start_time = time.time()
        FinalMedianCut.mediancut(img=img, lightSources=nLights, falloff=True)
        mComtime.append( time.time() - start_time)
        start_time = time.time()

        kmeans.main(img, 1024, nLights, True)
        kComtime.append(time.time() - start_time)
        if nLights==16:
            img2 = numpy.copy(img/255)
            resized = cv2.resize(img2, (256, 256), interpolation=cv2.INTER_AREA)
            img4D = numpy.empty((1, 256, 256, 3), dtype='uint8')
            img4D[0, :, :, :] = resized
            start_time = time.time()
            DeepLearningPython.deep_learning(img4D, nLights)
            cComtime.append(time.time() - start_time)
    data_set=[]
    if nLights!=16:
        data_set = {"nLigths": nLights, "mediancut": numpy.average(mComtime), "kmeans": numpy.average(kComtime), "cnn": 0}
    else:
        data_set = {"nLigths": nLights, "mediancut": numpy.average(mComtime), "kmeans": numpy.average(kComtime), "cnn": numpy.average(cComtime)}
    return data_set



path = "C:/Users/tobia/Desktop/Images/testdata/"
numofimages = 100

images = load_images_from_folder(path,numofimages)

data16 = compute(images,16)
data32 = compute(images,32)
data64 = compute(images,64)
data128 = compute(images,128)
data256 = compute(images,256)


t = PrettyTable(['nLigths', 'mediancut', "kmeans", "cnn"])
t.add_row(['16', data16.get('mediancut'), data16.get('kmeans'), data16.get('cnn')])
t.add_row(['32', data32.get('mediancut'), data32.get('kmeans'), "N/A"])
t.add_row(['64', data64.get('mediancut'), data64.get('kmeans'), "N/A"])
t.add_row(['128', data128.get('mediancut'), data128.get('kmeans'), "N/A"])
t.add_row(['256', data256.get('mediancut'), data256.get('kmeans'), "N/A"])
print(t)