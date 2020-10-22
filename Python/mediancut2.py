import struct
import cv2
import numpy as np


def drawRects(region, img):
    start_point = (region[0][0], region[0][0])
    end_point = np.shape(region)
   # print(start_point)
   # print(end_point)
    color = (255, 0, 0)
    thickness = 2
    img = cv2.rectangle(img, start_point, end_point, color, thickness)

    cv2.imshow("image", img)
    cv2.waitKey(0)


def mediancut():
    img = cv2.imread('image.jpg',cv2.IMREAD_GRAYSCALE)
    scale_percent = 15  # percent of original size
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    # resize image
    img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

    print(np.shape(img))

    # step 1
    regionList = []

    entireImg = img[:, :]

    regionList.append(entireImg)

   # print(np.shape(regionList[0]))
    step3(regionList, 3, img)


def step3(regionList, iterations, img):

    # step 3
    if iterations>0: # n
        # step 2
        for i in range (0,len(regionList)):
            #print (i)
            print ("hej " + str( regionList[0].cumsum(axis=0).cumsum(axis=1)))
            h, w = np.shape(regionList[0])
            if h > w:
                region1 =  regionList[0][:int(w/2)]

                region2 = regionList[0][int(w/2):]


                start_point1 = (0, 0)
                end_point1 = np.shape(region1)
                start_point2 = (end_point1[0], 0)

                x1, y1 = np.shape(region1)
                x2, y2 = np.shape(region2)



                end_point2 = x1+x2,y2
                print(end_point1)
                print(end_point2)

                color = (255, 255, 0)
                color2 = (0, 255, 0)
                thickness = 2
                img = cv2.rectangle(img, start_point1, end_point1, color, thickness)
                img = cv2.rectangle(img, start_point2, end_point2, color2, thickness)
                cv2.imshow("image", img)
                cv2.waitKey(0)

    cv2.imshow("image", img)
    cv2.waitKey(0)
mediancut()




""" 
def mediancut(img, nlights, falloff):
    if (nlights<1):
        nlights=-1

    if(falloff):
        falloff=0




def medianCutAux(xMin, xMax, yMin, yMax, iter):

    img = 0
    L=0
    ligths=[]
    lx=xMax-xMin
    ly= yMax-yMin

    if lx>2 and ly>2 and iter>0:
        rangeY = list(range(yMin, yMax))
        rangeX = list(range(xMin, xMax))
        L=np.array(rangeY,rangeX)
        tot = np.sum(np.sum(L))
        pivot=-1

        if lx>ly:
            #cut on the x-axis

            for i in range(xMin, xMax-1):
                rangeY = range(yMin, yMax)
                rangeX = range(xMin, i)
                L=np.array(rangeY,rangeX)
                c= np.sum(np.sum(L))
                if c>=(tot-c):
                    pivot=i

            if pivot==-1:
                pivot=xMax-1

            medianCutAux(xMin, pivot, yMin, yMax, iter-1)
            medianCutAux(pivot+1, xMax, yMin, yMax, iter - 1)

        else:
            # cut on the x-axis

            for i in range(yMin, yMax - 1):
                rangeY = range(yMin, i)
                rangeX = range(xMin, xMax)
                L = np.array(rangeY, rangeX)

                c = np.sum(np.sum(L))
                if c >= (tot - c):
                    pivot = i

            if pivot == -1:
                pivot = yMax - 1

            medianCutAux(xMin,xMax, yMin, pivot, iter - 1)
            medianCutAux(xMin,xMax, pivot+1, yMax, iter - 1)
    else:
        lights=[ligths, CreateLight(xMin, xMax, yMin, yMax, L, img)];


def CreateLight(xMin, xMax, yMin, yMax, L, img):
    tot=(yMax-yMin+1)*(xMax-xMin+1)
    rangeY = list(range(yMin, yMax))
    rangeX = list(range(xMin, xMax))
    tmpL = np.array(rangeY, rangeX)
    totL=np.sum(tmpL)

    if tot>0 and totL>0:
        # color value
        imgRange= np.array(rangeY, rangeX)
        col = np.reshape(imgRange, tot, 1, np.shape(img,3))
        value= np.sum(col,1)

        #position
        r,c = np.shape(col,1)
        X, Y = np.meshgrid(rangeY,rangeX)

        x_light= np.sum(np.sum(np.dot(tmpL, X))/totL*c)
        y_light = np.sum(np.sum(np.dot(tmpL, Y)) / totL * r)

        light= ("col:" + value, "x: " + x_light, "y: " + y_light, "x_bound: "+str( rangeX), "y bound: "+ str(rangeY))
        print(light)

    else:
        light=[]"""