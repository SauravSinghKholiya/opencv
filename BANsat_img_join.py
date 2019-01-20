import cv2
import numpy as np

'''im1 = cv2.imread("C:\\Users\\Dinesh\\Desktop\\ML\\sats\\bangladesh\\bang1maskupdate.jpg")
im2 = cv2.imread("C:\\Users\\Dinesh\\Desktop\\ML\\sats\\bangladesh\\bang2maskupdate.jpg")
im3 = cv2.imread("C:\\Users\\Dinesh\\Desktop\\ML\\sats\\bangladesh\\bang3maskupdate.jpg")
im4 = cv2.imread("C:\\Users\\Dinesh\\Desktop\\ML\\sats\\bangladesh\\bang4maskupdate.jpg")
im5 = cv2.imread("C:\\Users\\Dinesh\\Desktop\\ML\\sats\\bangladesh\\bang5maskupdate.jpg")
im6 = cv2.imread("C:\\Users\\Dinesh\\Desktop\\ML\\sats\\bangladesh\\bang6maskupdate.jpg")
im7 = cv2.imread("C:\\Users\\Dinesh\\Desktop\\ML\\sats\\bangladesh\\bang7maskupdate.jpg")'''

im1 = cv2.imread("C:\\Users\\Dinesh\\Desktop\\ML\\sats\\bangladesh\\bang1mask.jpg")
im2 = cv2.imread("C:\\Users\\Dinesh\\Desktop\\ML\\sats\\bangladesh\\bang2mask.jpg")
im3 = cv2.imread("C:\\Users\\Dinesh\\Desktop\\ML\\sats\\bangladesh\\bang3mask.jpg")
im4 = cv2.imread("C:\\Users\\Dinesh\\Desktop\\ML\\sats\\bangladesh\\bang4mask.jpg")
im5 = cv2.imread("C:\\Users\\Dinesh\\Desktop\\ML\\sats\\bangladesh\\bang5mask.jpg")
im6 = cv2.imread("C:\\Users\\Dinesh\\Desktop\\ML\\sats\\bangladesh\\bang6mask.jpg")
im7 = cv2.imread("C:\\Users\\Dinesh\\Desktop\\ML\\sats\\bangladesh\\bang7mask.jpg")

y = im1.shape[0]
x = im1.shape[1]
z = im1.shape[2]

demo=np.array([10,10,10])

def replace_white(i1,j1):
    arr1=np.array([255,255,255])
    im1[i1][j1] = arr1

def replace_black(i2,j2):
    arr2=np.array([0,0,0])
    im1[i2][j2] = arr2

for i in range(0,y):
    for j in range(0,x):
        if((im1[i][j] < demo).all() and (im2[i][j] < demo).all() and (im3[i][j] < demo).all() and (im4[i][j] < demo).all() and (im5[i][j] < demo).all() and (im6[i][j] < demo).all() and (im7[i][j] < demo).all()):
            replace_black(i,j)
        else:
            replace_white(i,j)

#print(im1)

cv2.imwrite("C:\\Users\\Dinesh\\Desktop\\ML\\sats\\bangladesh\\maskbangsjoin.jpg", im1)
        
