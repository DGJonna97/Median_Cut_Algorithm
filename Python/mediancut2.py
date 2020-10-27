import struct
import cv2
import numpy as np


#def drawRects(region, img):
    #start_point = (region[0][0], region[0][0])
    #end_point = np.shape(region)
   # print(start_point)
   # print(end_point)
    #color = (255, 0, 0)
    #thickness = 2
    #img = cv2.rectangle(img, start_point, end_point, color, thickness)

    #cv2.imshow("image", img)
    #cv2.waitKey(0)

def intensity(img):
    width = int(img.shape[1] )
    height = int(img.shape[0])
    tempimg = []
    print(tempimg)
    for i in range(0, height):
        row = []
        for j in range(0, width):
            pixel = img[i,j]
            pixelIntensity= 0.2125*pixel[0] + 0.7154*pixel[1] + 0.0721*pixel[2]
            row.append(round(pixelIntensity))
        tempimg.append(row)
    print("OG img shape " + str( np.shape(img)))
    print("ingensity img shape" + str(np.shape(tempimg)))
    return  tempimg


def SAT(region):
    sum = np.cumsum(region , axis=0)
    sum = np.cumsum(sum, axis=1)
    #print("sum: \n " + str(np.shape(sum)))
    return sum


def mediancut():
    img = cv2.imread('cheese.jpg',cv2.IMREAD_COLOR)
    img = intensity(img)


    regionList = []
    regionList.append(img)
    step3(regionList, 4)


def step3(regionList, iterations):

    # step 3
    if iterations>0: # n
        # step 2
        for i in range (0,len(regionList)):
            h, w = np.shape(regionList[i])
            if h< w:
                print("cutting y")
                # check sum of half the region  and compare it with the other half
                slicer= 2
                region = regionList[i]
                region1 = region[:][:int(h / slicer)]
                region2 = region[:][int(h / slicer):]


                value1 = np.argmax(SAT(region1))
                value11 = np.max(SAT(region1))
                value2 =  np.argmax(SAT(region2))
                value22 = np.max(SAT(region2))

                while not (np.abs(value1-value2)/value1) < 0.01:
                 #  print("value 1= " + str(value1))
                 #   print("value 2= " + str(value2))
                    if slicer<0:
                        print("failed")
                        break
                    if value1>value2:
                        slicer +=2
                    else:
                        slicer -=0.2
                    #print(slicer)
                    #region1 = region[:][:int(h / slicer)]
                    #region2 = region[:][int(h / slicer):]
                    #value1 = np.argmax(SAT(region1))
                    #value2 = np.argmax(SAT(region2))

                print("sat1: +" + str(value1))
                print("sat2: +" + str(value2))
                print("sat11: +" + str(value11))
                print("sat22: +" + str(value22))
                
                

                startpoint1 = np.shape(region1)[0], 0
                endpoint1 = np.shape(region1)
                print("start: +" + str(startpoint1))
                print("end: +" + str(endpoint1))
                color = (0, 255, 0)
                thickness = 9
                img = cv2.imread('cheese.jpg', cv2.IMREAD_COLOR)
                cv2.line(img, startpoint1, endpoint1, color, thickness)
                cv2.imshow("kraus", img)
                cv2.waitKey(0)
                regionList=[]
                regionList.append(region1)
                regionList.append(region2)
                step3(regionList,iterations-1)


            else:
                print("cutting x")
                # check sum of half the region  and compare it with the other half
                slicer = 2
                region = regionList[i]
                region1 = region[:int(w / slicer)][:]
                region2 = region[int(w / slicer):][:]

                value1 = np.argmax(SAT(region1))
                value11 = np.max(SAT(region1))
                value2 =  np.argmax(SAT(region2))
                value22 = np.max(SAT(region2))

                while not (np.abs(value1-value2)/value1) < 0.01:
                   # print("value 1= " + str(value1))
                  #  print("value 2= " + str(value2))
                    if slicer < 0:
                        print("failed")
                        break
                    if value1 > value2:
                        slicer += 2
                    else:
                        slicer -= 0.2
                    # print(slicer)
                    region1 = region[:][:int(h / slicer)]
                    region2 = region[:][int(h / slicer):]
                    value1 = np.argmax(SAT(region1))
                    value2 = np.argmax(SAT(region2))

                print("sat1: +" + str(value1))
                print("sat2: +" + str(value2))
                print("sat11: +" + str(value11))
                print("sat22: +" + str(value22))

                startpoint1 = 0, np.shape(region1)[1]
                endpoint1 = np.shape(region1)[1], np.shape(region1)[1]
                print("start: +" + str(startpoint1))
                print("end: +" + str(endpoint1))
                color = (0, 255, 0)
                thickness = 9
                img = cv2.imread('cheese.jpg', cv2.IMREAD_COLOR)
                cv2.line(img, startpoint1, endpoint1, color, thickness)
                cv2.imshow("kraus", img)
                cv2.waitKey(0)

                regionList = []
                regionList.append(region1)
                regionList.append(region2)
                step3(regionList, iterations - 1)
                print("commingcing itereations: " + iterations)
                # check sum of half the region  and compare it with the other half


            """
            print (i)
            print ("hej " + str( regionList[0].cumsum(axis=0).cumsum(axis=1)))
            h, w = np.shape(regionList[i])
            egionSAT= ComputeSummedAreaTable(regionList[i])
            boxx=w/4
            boxy=h/4
            currx=0

            for x in range (0,4):
                curry = 0
                for y in range(0, 4):
                #you are curently dividing the longest region in pixels and not light energi
                #light energy = weigthes average of the color channels of the light probe image
                #use a summed area table

                    start_point = int(currx), int(curry)
                    end_point = int(boxx+currx),int(boxy+curry)






                    color = (0, 255, 0)

                    thickness = 2
                    print(start_point)
                    print(end_point)
                    img = cv2.rectangle(img, start_point, end_point, color, thickness)
                    curry+=boxy
                currx+=boxx
            print("hej" + str(currx))

        cv2.imshow("image", img)
        cv2.waitKey(0)
                # do this after it works:
                # The latitude-longitude mapping over-represents regions near the
                #   poles. To compensate, the pixels of the probe image should first be
                # scaled by cosφ where φ is the pixel’s angle of inclination. Determining the longest dimension of a region should also take the overrepresentation into account;
                # this can be accomplished by weighting a regions width by cosφ for an inclination φ at center of the region.

    cv2.imshow("image", img)
    cv2.waitKey(0)"""
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