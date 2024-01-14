import os 
import cv2

img = cv2.imread(os.path.join('.','Imagenes', 'dog2.jpg'))
new_im = cv2.resize(img, (500,400))

print(new_im.shape)
#line
cv2.line(new_im, (80,120), (300,350), (0, 255, 0), 12)

# rectangle
cv2.rectangle(new_im, (60,200), (160,350), (0, 0, 255), 2)

#circle
cv2.circle(new_im, (350,350), 40, (255, 0, 0), -1)

#text
cv2.putText(new_im,"Hey you!", (100, 150), cv2.FONT_HERSHEY_TRIPLEX, 5, (200, 100, 0), 2)

cv2.imshow("Img", new_im)
cv2.waitKey(0)