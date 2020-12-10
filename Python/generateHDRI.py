import numpy as np
import cv2

def readImagesAndTimes(images):
    # List of exposure times
    times = np.array([1 / 30.0, 0.25, 2.5, 15.0], dtype=np.float32)
    imlist=[]
    for image in images:
        im = cv2.imread(image)
        imlist.append(im)

    return imlist, times


def generate(images, times):
    # Obtain Camera Response Function (CRF)
    calibrateDebevec = cv2.createCalibrateDebevec()
    for img in images:
        print (np.shape(img))
    responseDebevec = calibrateDebevec.process(images, times)

    # Merge images into an HDR linear image
    mergeDebevec = cv2.createMergeDebevec()
    hdrDebevec = mergeDebevec.process(images, times, responseDebevec)
    # Save HDR image.
    cv2.imwrite("hdrDebevec.hdr", hdrDebevec)
    return hdrDebevec


def main(images):
    imlist, times = readImagesAndTimes(images)
    hdr = generate(imlist, times)
    hdr = cv2.imread("hdrDebevec.hdr",-1)
    cv2.imshow("ost",hdr)
    cv2.waitKey(0)

filenames = ["im1.jfif", "im2.jfif", "im3.jfif", "im4.jfif"]
main(filenames)
