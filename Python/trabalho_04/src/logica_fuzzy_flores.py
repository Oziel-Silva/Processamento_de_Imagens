	# -*- coding: utf-8 -*-

##################################################################################
## Company: 
## Engineer: Oziel da Silva
## 
## Create Date: 24-09-2017 22:54 PM
## Module Name:logica_fuzzy_flores.py
## Description: implementação de logica fuzzy para realce de imagens
## Additional Comments:
## 
##################################################################################
import cv2
import numpy as np
import matplotlib.pyplot as plt

flores = cv2.imread("../img/flores.jpg")
flores2= np.zeros(((512,512)), dtype= np.uint8)

hist = cv2.calcHist([flores],[0], None, [256], [0,256])

for x in range(512):
	for y in range(512):
		if flores[x,y,1] <= 85:
			flores2[x,y] = 0
		elif ((85 < flores[x,y,1]) & (flores[x,y,1] <= 170)):
			flores2[x,y] = flores [x,y,1]
		elif (170 < flores[x,y,1]):
			flores2[x,y] = 255



plt.subplot(221)
plt.imshow(flores, cmap = "gray")
plt.title('Imagem sem Realce')

plt.subplot(222)
plt.imshow(flores2, cmap = "gray")
plt.title('Imagem com Realce')

plt.subplot(223)
plt.hist (flores.ravel (), 256, [0,256]);
plt.title('Histograma sem Realce')

plt.subplot(224)
plt.hist (flores2.ravel (), 256, [0,256]);
plt.title('Histograma com Realce')

plt.show ()