import os
import cv2
from PIL import Image
import numpy as np


def get_limits(color):
    c = np.uint8([[color]]) #insert bgr values to convert to hsv
    hsvC = cv2.cvtColor(c,  cv2.COLOR_BGR2HSV)

    lowerLimit = hsvC[0][0][0] - 10, 100, 100
    upperLimit = hsvC[0][0][0] + 10, 255, 255

    lowerLimit = np.array(lowerLimit, dtype = np.uint8)
    upperLimit = np.array(upperLimit, dtype = np.uint8)

    return lowerLimit, upperLimit

cap = cv2.VideoCapture(0)

yellow = [0,255,255] #yellow in BGR colorspace

while True:
    ret, frame = cap.read()

    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lowerLimit, upperLimit = get_limits(color=yellow)

    mask = cv2.inRange(hsvImage, lowerLimit, upperLimit) #location of pixels containing info we want

    mask_ = Image.fromarray(mask) #Converting image into pillow, diff format

    bbox = mask_.getbbox()

    if bbox is not None:
        x1, y1, x2, y2 = bbox
        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0), 5)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()