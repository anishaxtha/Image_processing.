# import numpy as np
# import cv2
# img=cv2.imread('images.png',0)
# cv2.imshow('originalImage',img)
# cv2.waitKey(0)


import numpy as np
import cv2
img=cv2.imread('huiwai.png',0)
w,h= img.shape
# print(w,h)
neg_img=np.array(img)
print(neg_img)
for x in range(w):
    for y in range(h):
        neg_img[x,y]=255-img[x,y]
cv2.imshow('originalImage',img)
cv2.imshow('Digitalnegative',neg_img)
cv2.waitKey(0)