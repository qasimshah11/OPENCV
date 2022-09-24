import numpy as np
import cv2 as cv
#the 0 in the brackets represents the camera
#entering a PATH in there will bring up a clip saved
cap = cv.VideoCapture(0)

#creating a circle
color = (0, 255, 0)
line_width = 3 #if we give value -1 it will be filled
radius = 100
point = (0, 0)


while True:
    #to actually make use of the camera we want to read from the camera stream
    ret, frame = cap.read()
    #we need to resize if need to and use fx and fy
    frame = cv.resize(frame, (0, 0), fx=0.5, fy=0.5)

    cv.circle(frame, point, radius, color, line_width)

    cv.imshow("frame", frame)

    ch =cv.waitKey(1)
    if ch & 0xFF == ord('q'):
        break

#we need this release function
cap.release()