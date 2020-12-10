import base64
import json
import time
import cv2
import zmq
import kmeans
import numpy
import FinalMedianCut
import os
from os.path import dirname
import DeepLearningPython

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

print("Server is listening...")
path = dirname(dirname(os.getcwd()))
i=1


#print(absolute_path)
while True:
    absolute_path = os.path.join(path, 'Documents', 'GitHub', 'Median_Cut_Algorithm', 'Unity',
                                 'Group 742 Visualization', 'Assets', 'Images', str(i) + '.jpg')
    #  Wait for next request from client
    message = socket.recv()
    x = "".join(map(chr, message)).split(",") #list where [0] = method, 16*[1] light sources, [2] which image


    #jpg_original = base64.b64decode(message)
   # jpg_as_np = np.frombuffer(message, dtype=np.uint8)
    #img = cv2.imdecode(jpg_as_np, flags=1)
    #cv2.imwrite('./0.jpg', img)

    img = []

    if x[2]==0:
        # choose image 1
        img = cv2.imread('stpetersangular.hdr', -1)
    else:
        # choose image 2
        img = cv2.imread("grace_probebetter.hdr", -1)


    dataset=[]
    if  int(x[0])==0:
        # run median cut
        print("running median cut")
        dataset = FinalMedianCut.mediancut(img=img, lightSources= pow(2,3+int(x[1])), falloff=True)
    elif int(x[0])==1:
        # run k means
        print("running kmeans")
        dataset = kmeans.main(img, 1024, pow(2,4+int(x[1])), True)
    else:
        # run deep learning
        print("running deep learning")
        img2 = numpy.copy(img)
        resized = cv2.resize(img2, (256,256), interpolation = cv2.INTER_AREA)

        img4D = numpy.empty((1, 256, 256, 3), dtype='uint8')

        img4D[0, :, :, :] = resized
        dataset = FinalMedianCut.mediancut(img=img, lightSources=pow(2, 3 + int(x[1])), falloff=True)

    print(dataset)

    #  Do some 'work'.
    #  Try reducing sleep time to 0.01 to see how blazingly fast it communicates
    #  In the real world usage, you just need to replace time.sleep() with
    #  whatever work you want python to do, maybe a machine learning task?
    #time.sleep(1)

    json_dump = json.dumps(dataset)

    #  Send reply back to client
    #  In the real world usage, after you finish your work, send your output here
    #cv2.imwrite(absolute_path, color)
    #img = cv2.imread(absolute_path)
    #cv2.imshow("ost", color)
    #cv2.waitKey(0)
    #regions = base64.b64decode(regions)
    socket.send_json(json_dump)
    i=i+1