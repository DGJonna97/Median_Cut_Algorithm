import FinalMedianCut
import os
import cv2
import csv
import shutil
import random
"""
def load_images_from_folder(folder):

    #amount = int(len(os.listdir(folder))*0.7)

    images = []
    folder2 = os.listdir(folder)
    random.shuffle(folder2)
    for i in range(0,len(folder2)):
        filename = folder2[i]
        img = cv2.imread(os.path.join(folder,filename))
        if img is not None:
            images.append(img)
        os.rename(folder+"/"+filename,  "C:/Users/tobia/Desktop/samepics/test/testy"+str(i)+".jpg")
        #shutil.move((folder+"/"+str(i)+".jpg"), "C:/Users/tobia/Desktop/Images/tranning")
    return images


images = load_images_from_folder("C:/Users/tobia/Desktop/samepics/test")

for img in images:
    centers = FinalMedianCut.mediancut(16, img, False)
    for ost in centers:
        with open('results.csv', 'a', newline='') as file:
            fieldnames = ['x', 'y']
            writer = csv.DictWriter(file, delimiter=";", fieldnames=fieldnames, dialect='excel')
            writer.writerow({'x': ost[0], 'y': ost[1]})"""

def load_images_from_folder(folder):

    #amount = int(len(os.listdir(folder))*0.7)

    images = []

    for i in range(0,len(folder)):
        folder2 = os.listdir(folder)
        filename = folder2[i]
        img = cv2.imread(os.path.join(folder,filename))
        os.rename(os.path.join(folder,filename),folder + "jpg"+filename+".jpg")


    return images


images = load_images_from_folder("C:/Users/tobia/Desktop/Illu/Xerox Scan_23112020200152.XSM/")
