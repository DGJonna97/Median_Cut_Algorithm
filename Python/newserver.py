#
#   Hello World server in Python
#   Binds REP socket to tcp://*:5555
#   Expects b"Hello" from client, replies with b"World"
#

import time
import zmq
import base64
import numpy as np
import cv2
#from cv2 import cv
from lib import lib
import FinalMedianCut

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    #  Wait for next request from client
    message = socket.recv()

    #jpg_original = base64.b64decode(message)
    jpg_as_np = np.frombuffer(message, dtype=np.uint8)
    img = cv2.imdecode(jpg_as_np, flags=1)
    cv2.imwrite('./0.jpg', img)

    #print("Received request: %s" % message)

    #  Do some 'work'.
    #  Try reducing sleep time to 0.01 to see how blazingly fast it communicates
    #  In the real world usage, you just need to replace time.sleep() with
    #  whatever work you want python to do, maybe a machine learning task?
    time.sleep(1)
    regions = FinalMedianCut.mediancut(img= img, lightSources=16, falloff=True)
    #  Send reply back to client
    #  In the real world usage, after you finish your work, send your output here
    print(regions)
    socket.send_string((regions.__repr__()))

