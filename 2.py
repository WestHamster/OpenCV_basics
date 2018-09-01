#VIDEO CAPTURING/READING

import cv2
import numpy as np

cap = cv2.VideoCapture(0)
#VIDEO WRITING
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))
#################
p=cap.isOpened()
while(True):
    ret,frame = cap.read()
    gray= cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)#RGB2BGR can also be done
    out.write(frame)
    fps = cap.get(cv2.CAP_PROP_FPS)
    print(fps)
    #print()
    size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    #print(size)
    #print()
    sat=cap.get(cv2.CAP_PROP_BRIGHTNESS)
    print(sat)
    #print()
    bright=cap.get(cv2.CAP_PROP_BRIGHTNESS)
    #print(bright)
    cv2.imshow('frame',frame)
    cv2.imshow('gray',gray)
    #for original
    #cv2.imshow('frame',frame)

    if cv2.waitKey(1) == ord('q'):
        break
#print(p)
cap.release()
out.release()
cv2.destroyAllWindows()



################

