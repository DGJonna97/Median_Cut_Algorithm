import statistics
import cv2
import numpy as np
import math


def intensity(img):
    # loop trough every pixel and modify the color values, before adding them together into intensity
    print("Finding intensity values of input image...")
    width = int(img.shape[1])
    height = int(img.shape[0])
    tempvalues = []
    greyimg = img  # greyscaled pic
    for i in range(0, height):
        row = []
        for j in range(0, width):
            pixel = img[i, j]
            pixelIntensity = 0.2125 * pixel[2] + 0.7154 * pixel[1] + 0.0721 * pixel[0]  # BGR image
            greyimg[i, j] = pixelIntensity
            row.append(pixelIntensity)
        tempvalues.append(row)
    #print("OG img shape " + str(np.shape(img)))
    #print("intensity values shape " + str(np.shape(tempvalues)))

    return tempvalues, greyimg  # returns 2d array of intensity values and the greyscaled img


def scaleforcos(intensitymap, img):
    print("Scaling the pixels of the input image by cosφ... ")
    # φ is the pixel’s angle of inclination...")
    height = int(img.shape[0])
    x = np.linspace(-(math.pi/2), math.pi/2, height)
    x = np.reshape(x, (height, 1))
    w = abs(np.cos(x))
    # print("w: " + str(np.shape(w)))
    # print("x: " + str(np.shape(x)))
    intensitymap = np.multiply(w, intensitymap)

    return intensitymap


def drawlights(xMin, xMax, yMin, yMax, grey):
    #draws a green circle at the center median of a regions x,y pos
   # img = cv2.imread('Bottles_Small.hdr', -1)  # reads BGR image
   # r=[]
   # g=[]
   # b=[]
    #for i in range(yMin, yMax):
    #    row = []
    #    for j in range(xMin, xMax):
     #       pixel = img[i, j]
     #       #print(pixel)
     #       #print(np.shape(pixel))
      #      r.append(pixel[2])
      #      g.append(pixel[1])
      #      b.append(pixel[0])

   # r = int(np.mean(r))
   # g = int(np.mean(g))
    #b = int(np.mean(b))

    center_coordinatesx = int(statistics.median([xMin, xMax]))
    center_coordinatesy = int(statistics.median([yMin, yMax]))
    global lightcount
    print("Placed light source  " + str(lightcount) + " at position (" + str(center_coordinatesx) + ", " + str(center_coordinatesy) + ")")
    cv2.circle(grey, (center_coordinatesx, center_coordinatesy), 3, (0, 255, 0), 1)

    lightcount+=1


def SAT(xMin, xMax, yMin, yMax, img):
    # Calculates a sum area table of the input region
    sum = []
    if xMin == xMax:
        for y in range(yMin, yMax):
            pixel = img[y][xMin]
            sum.append(pixel)
        return np.sum(sum)

    if yMin == yMax:
        for x in range(xMin, xMax):
            pixel = img[yMin][x]
            sum.append(pixel)
        return np.sum(sum)

    for x in range(xMin, xMax):
        for y in range(yMin, yMax):
            pixel = img[y][x]
            sum.append(pixel)

    return np.sum(sum)


def estimatelights(xMin, xMax, yMin, yMax, iterations, img, grey, falloff):
    # step 3, create regions compare their SAT, make sure there is the same SAT across regions, then make a cut
    lx = xMax - xMin
    ly = yMax - yMin

    if falloff:
        # do the cos with x calculations
        1+1
    #height = lx
   # x = np.linspace(-(math.pi), math.pi, height)
    # print(x)
    #x = np.reshape(x, (1, height))

   # lx = abs(np.cos(x))
    # print("w: " + str(np.shape(w)))
    # print("x: " + str(np.shape(x)))
    # print("intens: " + str(np.shape(intensitymap)))
   # lx = np.multiply(w, img[xMin:xMax])

    if (lx > 2 and ly > 2) and (iterations > 0):
        totalsum = SAT(xMin, xMax, yMin, yMax, img)
        cutpoint = -1

        if lx > ly:
            # cut on the X - axis
            for i in range(xMin, xMax - 1):
                regionsum = SAT(xMin, i, yMin, yMax, img)

                if regionsum >= (totalsum - regionsum):
                    cutpoint = i
                    break

            if cutpoint == -1:
                cutpoint = xMax - 1

            iterations = iterations - 1
            estimatelights(xMin, cutpoint, yMin, yMax, iterations, img, grey,falloff)
            estimatelights(cutpoint + 1, xMax, yMin, yMax, iterations, img, grey, falloff)

        else:
            # cut on the Y - axis
            for i in range(yMin, yMax - 1):
                regionsum = SAT(xMin, xMax, yMin, i, img)

                if regionsum >= (totalsum - regionsum):
                    cutpoint = i
                    break

            if cutpoint == -1:
                cutpoint = yMax - 1

            iterations = iterations - 1
            estimatelights(xMin, xMax, yMin, cutpoint, iterations, img, grey, falloff)
            estimatelights(xMin, xMax, cutpoint + 1, yMax, iterations, img, grey, falloff)

    else:
       # print("="*40)
       # print("Region: \n" + "xmin: " + str(xMin) + " xMax: " + str(xMax) + "\nYmin: " + str(yMin) + " Ymax: " + str(yMax))
        #cv2.rectangle(grey, (xMin, yMin), (xMax, yMax), (0, 254, 0), thickness=1)
        drawlights(xMin, xMax, yMin, yMax, grey)


def mediancut(lightSources, falloff=False):
    img = cv2.imread('Bottles_Small.hdr', -1)  # reads BGR image
    intensityMap, grey = intensity(img)  # returns 2d array of intensity values and the greyscaled image

    if falloff:
        intensityMap = scaleforcos(intensityMap, grey)

    # cv2.imshow("kraus", grey)  # comment this out if you dont want to keep closing grey image
    # cv2.waitKey(0)  # comment this out if you dont want to keep closing grey image

    r, c = np.shape(intensityMap)
    print("Estimating " + str(lightSources) + " light sources...")

    estimatelights(0, c, 0, r, round(np.log2(lightSources)), intensityMap, grey, falloff)

    cv2.imshow("Median Cut light sources", grey)
    #cv2.imwrite("Median Cut light sources.jpg", grey) save the light source pic
    cv2.waitKey(0)


global lightcount
lightcount = 1
mediancut(lightSources=256, falloff=True)
