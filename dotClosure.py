import cv2 as cv
from cv2 import COLOR_LAB2BGR,COLOR_BGR2LAB
morph_size = 0
video_capture = cv.VideoCapture(0,cv.CAP_DSHOW)
def increaseContrast(img):
    lab= cv.cvtColor(img, COLOR_BGR2LAB)
    l, a, b = cv.split(lab)
    clahe = cv.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
    cl = clahe.apply(l)
    limg=cv.merge((cl,a,b))
    final = cv.cvtColor(limg, COLOR_LAB2BGR)
    return final
def morphology_operations(image):
    morph_size =2

    morph_elem = cv.MORPH_RECT
    element = cv.getStructuringElement(morph_elem, (2*morph_size + 1, 2*morph_size+1), (morph_size, morph_size))
    operation = cv.MORPH_GRADIENT
    dst = cv.morphologyEx(image, operation, element)
    return dst
while True:
    ret,src = video_capture.read()
    if ret is None:
        print('Could not open or find the image')
        exit(0)
    image=morphology_operations(src)
    image=increaseContrast(image)
    cv.imshow("Video",image)
    if cv.waitKey(1)&0xFF==ord("q"):
        break
video_capture.release()
cv.destroyAllWindows()