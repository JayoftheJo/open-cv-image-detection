import cv2
import random
import numpy as np

#capturing a webcam/mp4 file
cap = cv2.VideoCapture(0)

#keeps the webcam displaying 
while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #displaying the frame
    cv2.imshow('frame', hsv)
    lower_blue = np.array([110, 50, 50])
    upper_blue = np.array([130, 255, 255])

    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    result = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow('frame', result)
    cv2.imshow('mask', mask)

    #if the key 
    if cv2.waitKey(1) == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()