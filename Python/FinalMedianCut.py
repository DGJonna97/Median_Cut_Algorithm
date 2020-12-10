import statistics
import cv2
import numpy as np
import math


def intensity(img):
    # loop trough every pixel and modify the color values, before adding them together into intensity
    #print("Finding intensity values of input image...")

    for pixel in img:
        0.2125 * pixel[2] + 0.7154 * pixel[1] + 0.0721 * pixel[0]
    return img[:, :, 0], img  # returns 2d array of intensity values and the original img


def scaleforcos(intensitymap, img):
    #print("Scaling the pixels of the input image by cosφ... ")
    # φ is the pixel’s angle of inclination...")
    height = int(img.shape[0])
    x = np.linspace(-(math.pi / 2), math.pi / 2, height)
    x = np.reshape(x, (height, 1))
    w = abs(np.cos(x))
    # print("w: " + str(np.shape(w)))
    # print("x: " + str(np.shape(x)))
    intensitymap = np.multiply(w, intensitymap)

    return intensitymap,w


def tonemapdatshit(ogimg):
    colors = []
    ogimg = cv2.imread("grace_probebetter.hdr", -1)
    r2 = []
    g2 = []
    b2 = []
    tonemapDurand = cv2.TonemapDurand(2.2)
    ldrDurand = tonemapDurand.process(ogimg)

    img = np.clip(ldrDurand * 255, 0, 255).astype('uint8')
    global regions
    for reg in regions:
        xMin, xMax, yMin, yMax = reg
        region_img = img[xMin:xMax, yMin:yMax]

        r = region_img[:, :, 2]
        g = region_img[:, :, 1]
        b = region_img[:, :, 0]

        r = int( np.average(r))
        g = int( np.average(g) )
        b = int (np.average(b) )

        r2.append(r)
        g2.append(g)
        b2.append(b)
        #center_coordinatesx = int(statistics.median([xMin, xMax]))
        #center_coordinatesy = int(statistics.median([yMin, yMax]))

        #cv2.circle(img, (center_coordinatesx, center_coordinatesy), 5, (b, g, r), -1)
        #cv2.circle(img, (center_coordinatesx, center_coordinatesy), 5, (0, 0, 0), 1)
    #cv2.imshow("fucking shitty tonemap", img)
    return r2,g2,b2

def vizualize(img):
    # draws a green circle at the center median of a regions x,y pos
    #r,g,b = tonemapdatshit(img)
    global regions
    for reg in regions:
        xMin, xMax, yMin, yMax = reg
        center_coordinatesx = int(statistics.median([xMin, xMax]))
        center_coordinatesy = int(statistics.median([yMin, yMax]))
        global lightcount
        #print("Placed light source  " + str(lightcount) + " at position (" + str(center_coordinatesx) + ", " + str(
        #    center_coordinatesy) + ")")
        #cv2.circle(img, (center_coordinatesx, center_coordinatesy), 5, (0, 255, 0), -1)
        #cv2.rectangle(img, (xMin, yMin), (xMax, yMax), (0, 255, 0), 1)

        lightcount += 1
    #cv2.imwrite("inputImageMedianCut2.jpg", color)

    return 0,0,0

def SAT(xMin, xMax, yMin, yMax, img):
    # Calculates a sum area table of the input region
    return np.sum(img[yMin:yMax, xMin:xMax])


def estimatelights(xMin, xMax, yMin, yMax, iterations, img, grey, falloff,w):
    # step 3, create regions compare their SAT, make sure there is the same SAT across regions, then make a cut
    lx = xMax - xMin
    ly = yMax - yMin

    if falloff:
        # do the cos with x calculations
      #  centerx = int((xMax + xMin)/2)
       # centery= int((yMax + yMin)/2)
        #weight = w[centerx-1]
        #weighty= w[centery - 1]
        #lx= weight*lx
        #ly = weighty*ly
        1+1

    # height = lx
    # x = np.linspace(-(math.pi), math.pi, height)
    # print(x)
    # x = np.reshape(x, (1, height))

    # lx = abs(np.cos(x))
    # print("w: " + str(np.shape(w)))
    # print("x: " + str(np.shape(x)))
    # print("intens: " + str(np.shape(intensitymap)))
    # lx = np.multiply(w, img[xMin:xMax])

    if (lx > 0.1 and ly > 2) and (iterations > 0):
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
            estimatelights(xMin, cutpoint, yMin, yMax, iterations, img, grey, falloff,w)
            estimatelights(cutpoint + 1, xMax, yMin, yMax, iterations, img, grey, falloff,w)

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
            estimatelights(xMin, xMax, yMin, cutpoint, iterations, img, grey, falloff,w)
            estimatelights(xMin, xMax, cutpoint + 1, yMax, iterations, img, grey, falloff,w)

    else:
        # print("="*40)
        # print("Region: \n" + "xmin: " + str(xMin) + " xMax: " + str(xMax) + "\nYmin: " + str(yMin) + " Ymax: " + str(yMax))
        global regions
        thisregion = xMin, xMax, yMin, yMax
        regions.append(thisregion)
        # drawlights(xMin, xMax, yMin, yMax, grey)


def mediancut(lightSources, img, falloff=False):
    global regions
    regions=[]
    #img = cv2.imread('Bottles_Small.hdr', -1)  # reads BGR image
    intensityMap, ogimg = intensity(img)  # returns 2d array of intensity values and the greyscaled image
    w=[]
    if falloff:
        intensityMap,w = scaleforcos(intensityMap, ogimg)

    # cv2.imshow("kraus", ogimg)  # comment this out if you dont want to keep closing ogimg image
    # cv2.waitKey(0)  # comment this out if you dont want to keep closing ogimg image

    r, c = np.shape(intensityMap)
    #print("Estimating " + str(lightSources) + " light sources...")

    estimatelights(0, c, 0, r, round(np.log2(lightSources)), intensityMap, ogimg, falloff,w)

    r,g,b = vizualize(ogimg)
    #cv2.imshow("Median Cut light sources", ogimg)
    #cv2.imwrite("Median Cut light sources.jpg", ogimg)
    #cv2.waitKey(0)

    centersx = []
    centersy = []
    for reg in regions:
        xMin, xMax, yMin, yMax = reg
        centersx.append( int(statistics.median([xMin, xMax])))
        centersy.append( int(statistics.median([yMin, yMax])))

    data_set = {"centerx": centersx,"centery": centersy, "red":r,  "green":g,  "blue":b}

    return data_set
    return color


global lightcount
global regions
lightcount = 1
regions =[]

#img = cv2.resize(img, (256,256), interpolation = cv2.INTER_AREA)

#cv2.waitKey(0)
img = cv2.imread('grace_probebetter.hdr', -1)
mediancut(64, img, True)
#cv2.imwrite("mediancutresult.jpg", img)
