import cv2
import numpy as np

img = cv2.imread('made7.png',0)
img = cv2.medianBlur(img,5)
cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
 
circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,10,
                            param1=20,param2=70,minRadius=0,maxRadius =0)
j = 0
x = 0
y = 0
circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    # draw the outer circle
    j+=1
    cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
    x+=i[0]
    y+=i[0]
x = (int(x/j))
y = (int(y/j))
cv2.circle(cimg,(x,y),2,(255,0,0),3)
print(j,x,y)
cv2.imshow('detected circles',cimg)
k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('/home/kriskim/Documents/Python/FindCircle/circled_eye.png',cimg)
    cv2.destroyAllWindows()