import cv2
import numpy as np

src = cv2.imread("C:/Users/master/Desktop/Test2.jpg", cv2.IMREAD_COLOR)
hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
h,s,v = cv2.split(hsv)
#mask = cv2.inRange(hsv, lower_blue, upper_blue)
mask = cv2.inRange(v,1,254)
mask2 = cv2.inRange(s,40,255)
mask3_up = cv2.inRange(h,180,180)
mask3_down = cv2.inRange(h,0,40)
mask3=(mask3_up+mask3_down)
# res = cv2.bitwise_and(src, src, mask=mask)
res = cv2.bitwise_and(src, src, mask=(mask))
res = cv2.bitwise_and(res, res, mask=(mask2))
res = cv2.bitwise_and(res, res, mask=mask3)
cv2.imshow('origin',src)
cv2.imshow('res',res)

# cv2.imshow('mask',mask) 
# cv2.imshow('mask2',mask2)
# cv2.imshow('mask3',mask3) 
cv2.waitKey(0)
cv2.destroyAllWindows()