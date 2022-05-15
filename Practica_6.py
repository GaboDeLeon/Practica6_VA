import cv2
import numpy as np

#Rojo
cap = cv2.imread('Rojo-mochila.jpeg')
capt = cv2.resize(cap, dsize=(480,680),interpolation=cv2.INTER_CUBIC)

hsv = cv2.cvtColor(capt, cv2.COLOR_BGR2HSV)
    
lower_red = np.array([30,150,50])
upper_red = np.array([255,255,180])
    
mask = cv2.inRange(hsv, lower_red, upper_red)
res = cv2.bitwise_and(capt,capt, mask= mask)

cv2.imshow('cap',capt)
cv2.imshow('mask',mask)
cv2.imshow('res',res)
    
cv2.waitKey(0)

cv2.destroyAllWindows()
cap.release()
