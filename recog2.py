import cv2
import sys
import math
from cv2 import COLOR_BGR2GRAY, COLOR_GRAY2BGR, COLOR_BGR2LAB,COLOR_LAB2BGR

import numpy as np
effect=[0,2,6]
display=0
cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)
video_capture = cv2.VideoCapture(0,cv2.CAP_DSHOW)
np.set_printoptions(threshold=sys.maxsize)
# print(sys.maxsize)
# print(cv2.CAP_DSHOW)
def increaseContrast(img):
    lab= cv2.cvtColor(img, COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)
    if display==1:
        cv2.imshow("lab",l)

    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
    cl = clahe.apply(l)
    # cv2.imshow('CLAHE output', cl)
    if 3 in effect:limg = cv2.merge((b,a,cl))
    elif 4 in effect:limg=cv2.merge((a,b,cl))
    elif 5 in effect:limg=cv2.merge((cl*(a+b),a,b))
    elif 6 in effect:limg=cv2.merge((cl*3,a,b))
    else: limg=cv2.merge((cl,a,b))
    if display==1:
        cv2.imshow("lab",limg)
    final = cv2.cvtColor(limg, COLOR_LAB2BGR)
    return final

def laplacianMagic(image):
    ddepth = cv2.CV_16S
    kernel_size = 3
    src=image
    # src = cv2.GaussianBlur(src, (3, 3), 0)
    src_gray = cv2.cvtColor(src, COLOR_BGR2GRAY)
    dst = cv2.Laplacian(src_gray, ddepth, ksize=kernel_size)
    abs_dst = cv2.convertScaleAbs(dst)
    abs_dst=cv2.cvtColor(abs_dst,COLOR_GRAY2BGR)
    return abs_dst
while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    # Draw a rectangle around the faces
    if 0 in effect:
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    if 1 in effect:
        frame=cv2.subtract(frame,laplacianMagic(frame))
    if 2 in effect:  
        frame=increaseContrast(frame)
    # Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()