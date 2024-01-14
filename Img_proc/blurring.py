import os
import cv2

new_im = cv2.imread(os.path.join('.','Imagenes','salt2.jpg'))
#print(img.shape)
#new_im = cv2.resize(img, (500,400))

k_size = 7
blrured_img = cv2.blur(new_im, (k_size, k_size))

gaus_blur = cv2.GaussianBlur(new_im, (k_size, k_size), 3)

median_blur = cv2.medianBlur(new_im, k_size)

cv2.imshow("bird", new_im)
cv2.imshow("blurred", blrured_img)
cv2.imshow("gaus", gaus_blur)
cv2.imshow("median", median_blur)
cv2.waitKey(0)
