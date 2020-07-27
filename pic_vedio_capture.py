
import cv2
print("Package imported")

img = cv2.imread("resources/1.jpg")
cv2.imshow("output",img)
cv2.waitKey(0)



cap = cv2.VideoCapture("resources/Peaky.mp4")
while True:
    success , img = cap.read()
    cv2.imshow("vedio",img)
    if cv2.waitKey(10) and 0xff==ord('q'):
        break
