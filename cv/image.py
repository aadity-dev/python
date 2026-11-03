#source .venv/bin/activate
import cv2
import numpy as np

img = cv2.imread('images/python.jpg')

#img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#print(type(img))
# imgBlue = img[:, :, 0]
# imgGreen = img[:, :, 1]
# imgRed = img[:, :, 2]
#img[:, :, 1] = 0 //to modify value on gray scale
#new_img = np.hstack((imgBlue,imgGreen, imgRed))

#img_resize = cv2.resize(img,(1920,1080))
#img_resize = cv2.resize(img, (img.shape[1]//2,img.shape[0]//2))
#to half the image size if you dont know the size of images

img_flip = cv2.flip(img, -1)


cv2.imshow("window", img_flip)
#print(img_resize.shape)
cv2.waitKey(2000)
