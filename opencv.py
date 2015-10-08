import cv2

img = cv2.imread('form.jpg',0)
#cv2.namedWindow('image', cv2.WINDOW_NORMAL)
#cv2.imshow('image',img)
#cv2.waitKey(0)
ball = img[172:668, 0:650]
cv2.imwrite('modi_fee.png',ball)
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image',ball)
cv2.waitKey(0)
cv2.destroyAllWindows()