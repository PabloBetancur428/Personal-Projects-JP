import os
import cv2


img_n = cv2.imread(os.path.join('.','Imagenes','flock.jpg'))
img_n = cv2.resize(img_n, (500,500))
img = cv2.cvtColor(img_n, cv2.COLOR_BGR2GRAY)


#img without filter
ret, thresh = cv2.threshold(img,0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

#with filter

blur = cv2.GaussianBlur(img, (5,5),0)
ret2, thresh2 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

contours, hierarchy = cv2.findContours(thresh2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

contour_img = cv2.drawContours(img_n, contours, 1, (0,255,0), 3)
print(contours)
for c in contours:
    if cv2.contourArea(c) > 50:
        x1, y1, w, h = cv2.boundingRect(c)
        cv2.rectangle(img_n,(x1,y1), (x1+w,y1+h),(255,0,0),2)



cv2.imshow("Otsu", thresh)
cv2.imshow("Otsu+gaussian", thresh2)
cv2.imshow("Contours", contour_img)

cv2.waitKey(0)