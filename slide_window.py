import cv2
import numpy as np

arr = cv2.imread("maskbangsjoin.jpg")
#cv2.imshow("im1",arr)
swsz=20
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
        if c<=10:
            repl(i,j)
        c=0

cv2.imshow("im",arr)
cv2.imwrite("maskbangsjoin_update.jpg",arr)
            


