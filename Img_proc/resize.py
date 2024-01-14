import cv2
import os

img = cv2.imread(os.path.join('.','Imagenes','toallin.jpg'))

resized_img = cv2.resize(img, (700,500))   #spicfy width and heigth

print(img.shape)# heigth and width
print(resized_img.shape)

cv2.imshow('img', img)
cv2.imshow('resized img', resized_img)
cv2.waitKey(0)
