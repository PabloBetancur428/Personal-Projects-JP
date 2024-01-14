import os
import cv2

#read webcam

webcam = cv2.VideoCapture(0) #if one, most likey would be 0. If more, other number

#visualize

while True:
    ret, frame = webcam.read()

    cv2.imshow('frame', frame)

    if cv2.waitKey(40) & 0xFF == ord('q'):
        break



webcam.release()
cv2.destroyAllWindows()