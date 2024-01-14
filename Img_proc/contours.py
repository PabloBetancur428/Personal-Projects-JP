import os
import cv2

img_n = cv2.imread(os.path.join('.','Imagenes','flock.jpg'))

img = cv2.cvtColor(img_n, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)

#wHEN we want to work with contours, me need the object to be white

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)



for cnt in contours:
    if cv2.contourArea(cnt) > 50:
        #cv2.drawContours(img_n, cnt, -1, (0, 255, 0), 2)
    #print(cv2.contourArea(cnt))
        x1, y1, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(img_n, (x1,y1), (x1 + w, y1 + h), (0,255,0), 2)
cv2.imshow("Img normal", img_n)

cv2.imshow("Thresh", thresh)

cv2.waitKey(0)