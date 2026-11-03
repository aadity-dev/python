#source .venv/bin/activate
import cv2
import numpy as np

img = cv2.imread('images/python.jpg')
print(type(img))

cv2.imshow("window", img)
cv2.waitKey(0)