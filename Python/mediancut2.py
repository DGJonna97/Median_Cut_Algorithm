import struct
import cv2
import numpy as np


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
            row.append(round(pixelIntensity))
        tempvalues.append(row)
    print("OG img shape " + str( np.shape(img)))
    print("intensity values shape" + str(np.shape(tempvalues)))

    return tempvalues, greyimg # returns 2d array of intensity values and the greyscaled img


def SAT(region):
    # calculate a sum area table of the input region
    sum = np.cumsum(region, axis=0)  # get the sum of one dimension
    sum = np.cumsum(sum, axis=1)  # get the sum of the other dimension
    # print("sum: \n " + str(np.shape(sum)))
    return sum  # returns the sum table


def mediancut():
    img = cv2.imread('download.jfif', cv2.IMREAD_COLOR) # reads BGR image
    intensityMap, grey = intensity(img) # returns 2d array of intensity values and the greyscaled image
    cv2.imshow("kraus", grey)  # comment this out if you dont want to keep closing grey image
    cv2.waitKey(0)  # comment this out if you dont want to keep closing grey image
    regionList = [] # step 1
    regionList.append(intensityMap)  # step 1
    step3(regionList, 4, grey)
    cv2.imshow("kraus", grey)
    cv2.waitKey(0)


def step3(regionList, iterations, img):
    # takes in list of regions and n

    # step 3
    if iterations > 0:  # n
        # step 2
        for i in range(0, len(regionList)):
            h, w = np.shape(regionList[i])
            if h < w:
                print("cutting y")
                # check sum of half the region  and compare it with the other half
                slicer = 2 # controls where the cut happens
                region = regionList[i]  # get region object out of the list
                region1 = region[:][:int(h / slicer)]  # split the region up into two regions
                region2 = region[:][int(h / slicer):]

                value1 = np.argmax(SAT(region1))  # returns index of the highest value in the array
                value11 = np.max(SAT(region1))  # returns the highest value in the array
                value2 = np.argmax(SAT(region2))
                value22 = np.max(SAT(region2))

                while not (np.abs(value1 - value2) / value1) < 0.01:  #make sure its not negative
                    #  print("value 1= " + str(value1))
                    #   print("value 2= " + str(value2))
                    if slicer < 0:
                        print("failed")
                        break
                    if value1 > value2:
                        slicer += 2
                    else:
                        slicer -= 0.2
                    # print(slicer)
                    # region1 = region[:][:int(h / slicer)]
                    # region2 = region[:][int(h / slicer):]
                    # value1 = np.argmax(SAT(region1))
                    # value2 = np.argmax(SAT(region2))

                print("sat1: +" + str(value1))
                print("sat2: +" + str(value2))
                print("sat11: +" + str(value11))
                print("sat22: +" + str(value22))

                # attempt to draw a line, should probably be own func
                startpoint1 = np.shape(region1)[0], 0 # start x,y of line. shape of region1[0] = width or maybe height?
                endpoint1 = np.shape(region1) # end x,y of line
                print("start: +" + str(startpoint1))
                print("end: +" + str(endpoint1))
                color = (0, 255, 0)
                thickness = 9
                cv2.line(img, startpoint1, endpoint1, color, thickness)
                #cv2.imshow("kraus", img)
                #cv2.waitKey(0)

                # prepare for the next cut by adding these two regions to the list  and running the func again
               # regionList = []
                regionList.append(region1)
                regionList.append(region2)
                iterations=iterations-1
                print("commencing iteration: " +  str(iterations))

                step3(regionList, iterations, img)


            else:
                print("cutting x")
                # check sum of half the region  and compare it with the other half
                slicer = 2
                region = regionList[i]
                region1 = region[:int(w / slicer)][:]
                region2 = region[int(w / slicer):][:]

                value1 = np.argmax(SAT(region1))
                value11 = np.max(SAT(region1))
                value2 = np.argmax(SAT(region2))
                value22 = np.max(SAT(region2))

                while not (np.abs(value1 - value2) / value1) < 0.01:
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
                cv2.line(img, startpoint1, endpoint1, color, thickness)
                #cv2.imshow("kraus", img)
                #cv2.waitKey(0)

                #regionList = []
                regionList.append(region1)
                regionList.append(region2)
                iterations = iterations - 1
                print("commencing iteration: " + str(iterations))
                step3(regionList, iterations - 1, img)



mediancut()
"""
#below lines draws 4x4 boxes
for x in range (0,4):
print (i)
print ("hej " + str( regionList[0].cumsum(axis=0).cumsum(axis=1)))
h, w = np.shape(regionList[i])
egionSAT= ComputeSummedAreaTable(regionList[i])
boxx=w/4
boxy=h/4
currx=0
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

