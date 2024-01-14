import os
import cv2

img = cv2.imread(os.path.join('.','Imagenes','bird.jpg'))
print(img.shape)
new_im = cv2.resize(img, (500,400))

#Convert to another colorspace

img_rgb = cv2.cvtColor(new_im, cv2.COLOR_BGR2RGB)

img_gray = cv2.cvtColor(new_im, cv2.COLOR_BGR2GRAY) #having the info from 3 channels, into one 
img_hsv = cv2.cvtColor(new_im, cv2.COLOR_BGR2HSV)
cv2.imshow('Imagen',new_im)
cv2.imshow('ImagenHSV',img_hsv)
#cv2.imshow('ImagenGray',img_gray)
#cv2.imshow('Imagen BGR TO RGB',img_rgb)
cv2.waitKey(0)