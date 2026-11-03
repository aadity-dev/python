#source .venv/bin/activate
import cv2
import numpy as np

img = cv2.imread('images/python.jpg')

#img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#print(type(img))

imgBlue = img[:, :, 0]
imgGreen = img[:, :, 1]
imgRed = img[:, :, 2]
#img[:, :, 1] = 0 //to modify value on gray scale

new_img = np.hstack((imgBlue,imgGreen, imgRed))

cv2.imshow("window", new_img)

cv2.waitKey(3000)
