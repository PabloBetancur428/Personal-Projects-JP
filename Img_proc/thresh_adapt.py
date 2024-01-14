import os 
import cv2

new_im = cv2.imread(os.path.join('.','Imagenes', 'sud.png'))
#new_im = cv2.resize(img, (500,400))

#convert into grayscale
gray_img = cv2.cvtColor(new_im, cv2.COLOR_BGR2GRAY)
ret, thresh1 = cv2.threshold(gray_img, 150, 255, cv2.THRESH_BINARY)

thresh = cv2.adaptiveThreshold(gray_img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 51, 20)
thresh2 = cv2.adaptiveThreshold(gray_img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 51, 50)
#cv2.imshow("img", new_im)
cv2.imshow("thresh", thresh)
#cv2.imshow("thresh1", thresh1)
cv2.imshow("thresh2", thresh2)
cv2.waitKey(0)
