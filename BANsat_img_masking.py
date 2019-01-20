import cv2
import numpy as np

im = cv2.imread("bang7.jpg")

hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)


#for light blue shades use:
'''lower_blue = np.array([110,0,0])
upper_blue = np.array([130,255,255])'''

#for darker water bodies use:
'''lower_blue=np.array([56,80,0],np.uint8)
upper_blue=np.array([170,255,255],np.uint8)'''


#for blue water bodies use:
lower_blue=np.array([96,130,0],np.uint8)
upper_blue=np.array([140,255,255],np.uint8)

'''#for darker blue water bodies use:
lower_blue=np.array([96,110,0],np.uint8)
upper_blue=np.array([150,255,255],np.uint8)'''


# Threshold the HSV image to get only blue colors
mask = cv2.inRange(hsv, lower_blue, upper_blue)

# Bitwise-AND mask and original image
res = cv2.bitwise_and(im,im, mask= mask)

mask = cv2.resize(mask, (0,0), fx=0.4, fy=0.4)
im = cv2.resize(im, (0,0), fx=0.4, fy=0.4)
res = cv2.resize(res, (0,0), fx=0.4, fy=0.4)

cv2.imwrite("bang7mask.jpg",mask)
    
cv2.imshow('frame',im)
cv2.imshow('mask',mask)
#cv2.imshow('res',res)

arr = cv2.imread("bang7mask.jpg")
#cv2.imshow("im1",arr)
swsz=35
def repl(i,j):
    arr2= np.array([0,0,0])
    for i1 in range(i,i+swsz):
        for j1 in range(j,j+swsz):
            arr[i1][j1] = arr2


y = arr.shape[0]
x = arr.shape[1]
z = arr.shape[2]


c=0
for i in range(0,y-(swsz-1),swsz):
    for j in range(0,x-(swsz-1),swsz):
        for i1 in range(i,i+swsz):
            for j1 in range(j,j+swsz):
                if (arr[i1][j1] > np.array([240,240,240])).all():
                    c +=1
        if c<=1:
            repl(i,j)
        c=0

cv2.imshow("im",arr)
cv2.imwrite("bang7maskupdate.jpg",arr)
            


