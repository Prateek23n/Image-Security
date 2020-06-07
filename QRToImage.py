import cv2
from PIL import Image
import numpy as np
#import ImageToQR
import time
#print("Data:",ImageToQR.data)
# initalize the cam

# initialize the cv2 QRCode detector

result=True
image=cv2.imread('QR.png')
detector = cv2.QRCodeDetector()
    # detect and decode
data, bbox, x = detector.detectAndDecode(image)
    #print("Data:",data)
    #if(bbox is not None):
        # display the image with lines
        #for i in range(len(bbox)):
            # draw all lines
         #   cv2.line(image, tuple(bbox[i][0]), tuple(bbox[(i+1) % len(bbox)][0]), color=(255, 0, 0), thickness=2)
        #if(data):
            #print("[+] QR Code detected, data:", data)
cv2.imshow("Image",image)
cv2.waitKey(0) 
        
# check if there is a QRCode in the image
if(data):
    qr_code=input("Enter the password:")
    if(qr_code==data):
        print("Correct Password...")
        time.sleep(1)
        print("Creating Image")
        image_data=np.load('data.npy')
        get_val=Image.fromarray(image_data)
        get_val.save("Decoded Picture.png")
        #cv2.imshow("Decoded Picture.png")    
        cv2.waitKey(1)
        
    else:
        print("Wrong Password...")
#cv2.release()
cv2.destroyAllWindows()
