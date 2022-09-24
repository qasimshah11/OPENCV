import numpy as np
import cv2 as cv
#the 0 in the brackets represents the camera
#entering a PATH in there will bring up a clip saved
cap = cv.VideoCapture(0)

while True:
    #to actually make use of the camera we want to read from the camera stream
    ret, frame = cap.read()
    #we need to resize if need to and use fx and fy
    frame = cv.resize(frame, (0,0), fx=0.5, fy=0.5)

    cv.imshow("frame", frame)

    ch =cv.waitKey(1)
    if ch & 0xFF == ord('q'):
        break

#we need this release function
cap.release()