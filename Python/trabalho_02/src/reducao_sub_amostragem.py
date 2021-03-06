    # -*- coding: utf-8 -*-

##################################################################################
## Company: 
## Engineer: Oziel da Silva
## 
## Create Date: 02-09-2017 14:26 AM
## Module Name:redução por sub amostragem 
## Description: redução de imagem usando o método da sub amostragem
## Additional Comments:
## 
##################################################################################
import cv2
import matplotlib.pyplot as plt
import numpy as np

lena_512 = cv2.imread("../img/lena_gray_512.tif")
woman_512 = cv2.imread("../img/woman_blonde.tif")

reducao1 = 1/2
reducao2 = 1/4
reducao3 = 1/8
reducao4 = 1/16

lena_256 = np.zeros(((256,256)), dtype=np.uint8)
lena_128 = np.zeros(((128,128)), dtype=np.uint8)
lena_64 = np.zeros(((64,64)), dtype=np.uint8)
lena_32 = np.zeros(((32,32)), dtype=np.uint8)

woman_256 = np.zeros(((256,256)), dtype=np.uint8)
woman_128 = np.zeros(((128,128)), dtype=np.uint8)
woman_64 = np.zeros(((64,64)), dtype=np.uint8)
woman_32 = np.zeros(((32,32)), dtype=np.uint8)

for  i in range(0, 256):
    for j in range(0, 256):
        lena_256[i,j] = lena_512[int(i/reducao1),int(j/reducao1),1]
        woman_256[i,j] = woman_512[int(i/reducao1),int(j/reducao1),1]

cv2.imwrite('../img/lena_256.tif', lena_256)
cv2.imwrite('../img/woman_256.tif', woman_256)


for  i in range(0, 128):
    for j in range(0, 128):
        lena_128[i,j] = lena_512[int(i/reducao2),int(j/reducao2),1]
        woman_128[i,j] = woman_512[int(i/reducao2),int(j/reducao2),1]
cv2.imwrite('../img/lena_128.tif', lena_128)
cv2.imwrite('../img/woman_128.tif', woman_128)


for  i in range(0, 64):
    for j in range(0, 64):
        lena_64[i,j] = lena_512[int(i/reducao3),int(j/reducao3),1]
        woman_64[i,j] = woman_512[int(i/reducao3),int(j/reducao3),1]


cv2.imwrite('../img/lena_64.tif', lena_64)
cv2.imwrite('../img/woman_64.tif', woman_64)


for  i in range(0, 32):
    for j in range(0, 32):
        lena_32[i,j] = lena_512[int(i/reducao4),int(j/reducao4),1]
        woman_32[i,j] = woman_512[int(i/reducao4),int(j/reducao4),1]

cv2.imwrite('../img/lena_32.tif', lena_32)
cv2.imwrite('../img/woman_32.tif', woman_32)


print (lena_512.shape)
print (woman_512.shape)
print (lena_256.shape)
print (woman_256.shape)
print (lena_128.shape)
print (woman_128.shape)
print (lena_64.shape)
print (woman_64.shape)
print (lena_32.shape)
print (woman_32.shape)

plt.subplot(221)
plt.imshow(lena_256,cmap = "gray")
plt.subplot(222)
plt.imshow(lena_128, cmap = "gray")
plt.subplot(223)
plt.imshow(lena_64, cmap = "gray")
plt.subplot(224)
plt.imshow(lena_32, cmap = "gray")
plt.show()
