import os
import cv2
import numpy as np

img = cv2.imread(os.path.join('.','Imagenes', 'dog2.jpg'))
new_im = cv2.resize(img, (500,400))

img_edg = cv2.Canny(new_im, 100, 190)

img_edge_d = cv2.dilate(img_edg, np.ones((3,3), dtype= np.int8))

img_edge_e = cv2.erode(img_edge_d, np.ones((5,5), dtype= np.int8))

cv2.imshow("img",new_im)
cv2.imshow("img_edge",img_edg)
cv2.imshow("img_edge_d",img_edge_d)
cv2.imshow("img_edge_e",img_edge_e)
cv2.waitKey(0)