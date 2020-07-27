#grayscale, blur, canny, dialated
import cv2
import numpy as np
kernel =  np.ones((5,5),np.uint8)
print("Package imported")

img = cv2.imread("resources/1.jpg")


imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
imgcanny = cv2.Canny(img,100,100)
imgdail = cv2.dilate(imgcanny,kernel,iterations=1)


cv2.imshow("gray Image",imgGray)
cv2.imshow("blur Image",imgBlur)
cv2.imshow("CANNY",imgcanny)
cv2.imshow("image dialation",imgdail)
cv2.waitKey(0)