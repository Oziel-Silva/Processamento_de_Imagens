	# -*- coding: utf-8 -*-

##################################################################################
## Company: 
## Engineer: Oziel da Silva
## 
## Create Date: 03-09-2017 11:40 AM
## Module Name:Redução de Nivel de Cinza 
## Description: 
## Additional Comments:
## 
##################################################################################

import cv2
import matplotlib.pyplot as plt
import numpy as np

lena_512 = cv2.imread("../img/lena_gray_512.tif",0)
lena_4   = np.zeros(((512,512)), dtype= np.uint8)

lena_4 = np.uint8(lena_512/16)
lena_2 = np.uint8(lena_512/64)
lena_1 = np.uint8(lena_512/128)



plt.subplot(221)
plt.imshow(lena_512,cmap = "gray")
plt.subplot(222)
plt.imshow(lena_4, cmap = "gray")
plt.subplot(223)
plt.imshow(lena_2, cmap = "gray")
plt.subplot(224)
plt.imshow(lena_1, cmap = "gray")

cv2.imwrite('../img/lena_4_bits.tif', lena_4)
cv2.imwrite('../img/lena_2_bits.tif', lena_2)
cv2.imwrite('../img/lena_1_bit.tif', lena_1)



plt.show()
