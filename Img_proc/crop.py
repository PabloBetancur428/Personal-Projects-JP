import cv2
import os


img = cv2.imread(os.path.join('.','Imagenes','toallin.jpg'))

print(img.shape)

cropped_img = img[50:100, 50:180]

cv2.imshow('img', img)
cv2.imshow('cropped', cropped_img)
cv2.waitKey(0)