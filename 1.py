import cv2
import matplotlib.pyplot as plt

img = cv2.imread('C:/Users/WestHamster/Desktop/STUDY/front-end/background.jpg',cv2.IMREAD_GRAYSCALE)
cv2.imshow('image',img)

#################################################################
#For changing bgr to rgb #                                      #
##########################                                      #
##img = cv2.imread('background.jpg')                            #
##b,g,r = cv2.split(img)                                        #
##img2 = cv2.merge([r,g,b])                                     #
##plt.subplot(121);plt.imshow(img) # expects distorted color    #
##plt.subplot(122);plt.imshow(img2) # expect true color         #
##plt.show()                                                    #
                                                                #
##cv2.imshow('bgr image',img) # expects true color              #
##cv2.imshow('rgb image',img2) # expects distorted color        #
##cv2.waitKey(0)                                                #
##cv2.destroyAllWindows()                                       #
##cv2.cvtColor(img,COLOR_BGR2RGB)                               #
#################################################################

k=cv2.waitKey(0)
if k==27:
    cv2.destroyAllWindows()
elif k==ord('s'):
    cv2.namedWindow('image',cv2.WINDOW_SMALL)
    cv2.imwrite('loophole.png',img)
    cv2.destroyAllWindows()

    
##plt.imshow(img,cmap='gray',interpolation='bicubic')
##plt.plot([70,950],[90,750],'c',linewidth=5)
##plt.show()
