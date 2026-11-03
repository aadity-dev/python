#source .venv/bin/activate
import cv2
import numpy as np

img = cv2.imread('images/python.jpg')

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print(type(img))


cv2.imshow("window", img_gray)
cv2.waitKey(3)
