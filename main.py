import cv2
vid = cv2.VideoCapture(0,cv2.CAP_DSHOW)
image=cv2.imread("missingTexture.jpg")
while(True):
      
    ret, frame = vid.read()
    if ret:
        cv2.imshow('frame', frame)
    else:
        cv2.imshow("frame",image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
vid.release()
cv2.destroyAllWindows()