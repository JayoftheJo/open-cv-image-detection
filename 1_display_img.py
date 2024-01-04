import cv2
import random
import numpy as np

img = cv2.imread('images/valorant.jpg', -1) #brings the img into program
img = cv2.resize(img, (5, 5), fx=0.5, fy=0.5) #used to resize the img - 1st param: the img, 2nd param: x/y size, 3rd param: based on size of img
img = cv2.rotate(img, cv2.cv2.ROTATE_90_COUNTERCLOCKWISE) #used to rotate the img
cv2.imwrite('new_img.jpg', img) #renaming the img file
cv2.imshow('Image', img) # displays the img to user

cv2.waitKey(0) #waits n seconds until going to next line or a key is pressed (0 means infinite)
cv2.destroyAllWindows() #closes the window

print(img[40][45]) #accessing a specific pixel of an img

for i in range(100):
    for j in range(img.shape[1]):
        img[i][j] = [random.randint(255), random.randint(255), random.randint(255)]    

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#copying a part of img and pasting it elsewhere in img
part = img[500:700, 600:900]
img[100:300, 650:950] = part
