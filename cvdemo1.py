import cv2 as cv


# #reads the image from PATH
# img = cv.imread('Photos/Cat03.jpg')
#
# #shows the image
# cv.imshow('Cat03', img)
#
# #Keyboard binding function - waits for a delay for a key to be pressed - 0 means it will wait for a long time
# cv.waitKey(0)
#
# #important to know the dimensions of image

#----------------------------------------------------------------------------------------------------------------------

#READING VIDEOS

capture= cv.VideoCapture('Videos/vid4.mp4')#you would use 0 to reference you webcam

#to read image you need a while loop to read the video frame by frame

while True:
    isTrue, frame = capture.read()  #isTrue sees if the video was read successfully or not #capture.read() returns the frame
    cv.imshow('Video', frame) # releases each frame
    #to stop the .read reading indefinetly we need to write:

    if cv.waitKey(20) & 0xFF==ord('d'): # if the letter d is pressed break
        break
capture.release()
cv.destroyAllWindows()

#we get an Assertion erorr which means opencv cannot find a media file --> running out of frame