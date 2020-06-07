import numpy as np
import cv2
image_capture=cv2.VideoCapture(0)
result=True
while(True):
    cap,frame=image_capture.read()
    cv2.imshow('Webcam',frame)
    if(cv2.waitKey(1) & 0xFF==ord('q')):
        cv2.imwrite('Picture.png',frame)
        break
    #result=False
image_capture.release()
cv2.destroyAllWindows()
print("Frame:",frame)
print("Size:",frame.size)
print("Shape:",frame.shape)
