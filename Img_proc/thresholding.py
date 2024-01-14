import cv2
import os

img = cv2.imread(os.path.join('.','Imagenes','letter.jpg'))
print(img.shape)
new_im = cv2.resize(img, (500,400))

#convert into gray

gray_img = cv2.cvtColor(new_im, cv2.COLOR_BGR2GRAY)

#APPLYING THRESHOLD

ret, thresh = cv2.threshold(gray_img, 60, 255, cv2.THRESH_BINARY)

thresh = cv2.blur(thresh, (10,10))

ret, thresh = cv2.threshold(thresh, 70, 255, cv2.THRESH_BINARY)

cv2.imshow("Img", gray_img)
cv2.imshow("Img", thresh)
cv2.waitKey(0)