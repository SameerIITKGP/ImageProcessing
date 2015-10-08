import numpy as np
import cv2

im = cv2.imread('1750024.jpg')

height, width, depth = im.shape

imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)
imgray = cv2.bilateralFilter(imgray,11,17,17)
imgray = cv2.Canny(imgray,30,200)
contours, hierarchy = cv2.findContours(imgray, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cnts = sorted(contours, key = cv2.contourArea, reverse = True)[:10]
screenCnt = None
for c in cnts:
	peri = cv2.arcLength(c, True)
	approx = cv2.approxPolyDP(c, 0.02 * peri, True)
	if len(approx) == 4:
		if ((approx[0][0][1] < height/2) and (approx[2][0][1] < height/2) and (approx[0][0][0] > width/2) and (approx[2][0][0] > width/2)):
			screenCnt = approx
			break

l1 = screenCnt[0][0][0]
t1 = screenCnt[0][0][1]
r1 = screenCnt[2][0][0]
b1 = screenCnt[2][0][1]
b1 = b1 - (t1-b1)/2.3



#cv2.drawContours(im, contours, -1, (0,255,0), 3)
cv2.namedWindow('image')
#cv2.imshow('image',im[330:830, 810:1100])
image = im[t1:b1, l1:r1]
cv2.imshow('image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()