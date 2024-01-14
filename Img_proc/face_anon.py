import cv2
import os
import mediapipe as mp


output_dir = './output'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# read image
img = cv2.imread(os.path.join('.','Imagenes','face.jpg'))

H, W, _ =img.shape
#cv2.imshow("img",img)
#cv2.waitKey(0)

# detect faces
face_detector = mp.solutions.face_detection

with face_detector.FaceDetection(min_detection_confidence= 0.5, model_selection = 0) as face_detection:

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    out = face_detection.process(img_rgb)

    if out.detections is not None:
        for detection in out.detections:
            location_data = detection.location_data
            bbox = location_data.relative_bounding_box

            x1, y1, w, h = bbox.xmin, bbox.ymin, bbox.width, bbox.height
            #convert relative values to int values according to image dimensions
            x1 = int(x1*W)
            y1 = int(y1*H)
            w = int(w*W)
            h = int(h*H)

            #img = cv2.rectangle(img, (x1, y1), (x1+w, y1+h), (0,255,0),5)
            # blur face 
            img[y1:y1+h, x1:x1+w, :] = cv2.blur(img[y1:y1+h, x1:x1+w, :], (50,50))
    #cv2.imshow('img', img)
    #cv2.waitKey(0)



# save image
cv2.imwrite(os.path.join(output_dir, 'blurred_faces.png'), img)