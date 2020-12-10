import kmeans
import os
import cv2
import csv
import shutil
import random


def load_images_from_folder(folder):

    #amount = int(len(os.listdir(folder))*0.7)

    images = []
    folder2 = os.listdir(folder)
    #random.shuffle(folder2)
    for i in range(0,len(folder2)):
        filename = folder2[i]
        img = cv2.imread(os.path.join(folder,filename),-1)
        if img is not None:
            images.append(img)
            #shutil.copy2(folder+"/"+filename, os.path.dirname(os.path.dirname(folder))+"/"+ str(nLights))

        #shutil.move((folder+"/"+str(i)+".jpg"), "C:/Users/tobia/Desktop/Images/tranning")
    return images

nLights = 32 # how many light sources
path = "C:/Users/tobia/Desktop/samepics/trainning/" # path of the samepics/trainnig folder

images = load_images_from_folder(path)
for img in images:

    centers = kmeans.main(img,1024,nLights,True)
    for cen in centers:
        with open(os.path.dirname(os.path.dirname(path))+"/results"+ str(nLights)+".csv", 'a', newline='') as file:
            fieldnames = ['x', 'y']
            writer = csv.DictWriter(file, delimiter=";", fieldnames=fieldnames, dialect='excel')
            writer.writerow({'x': int(cen[0]), 'y': int(cen[1])})

