import cv2 as cv

img = cv.imread('Photos/Cat03.jpg')
cv.imshow('Cat03', img)

def rescaleFrame(frame, scale = 0.75):
    # Images, Videos and Live Video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA) #resizing the fram the a particular dimension
resized_img = rescaleFrame(img)
cv.imshow('Image resized', resized_img)
#READING VIDEOS
capture= cv.VideoCapture('Videos/vid4.mp4')
#
# while True:
#
#     isTrue, frame = capture.read()
#
#     frame_resized = rescaleFrame(frame)
#
#     #cv.imshow('Video', frame)
#     #New resized Video
#     cv.imshow('Video Resized', frame_resized)
#
#     if cv.waitKey(20) & 0xFF==ord('d'): # if the letter d is pressed break
#         break
# capture.release()
# cv.destroyAllWindows()

#ANOTHER WAY OF RESIZED FOR VIDEOS USING .set
def changesRes(width,height):
    # Live Video
    capture.set(3,width)
    capture.set(4,height)



cv.waitKey(0)

