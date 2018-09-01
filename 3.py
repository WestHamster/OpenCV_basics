import numpy as np
import cv2

img = cv2.imread('C:/Users/WestHamster/Desktop/STUDY/front-end/bckgrnd1.jpg',cv2.IMREAD_COLOR)

cv2.line(img,(0,0),(150,150),(0,0,255),20)


cv2.rectangle(img, (15,20), (200,150),(255,0,0), 15)

cv2.circle(img, (150,70),45 , (0,255,0), -1, 15)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
