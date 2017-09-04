	# -*- coding: utf-8 -*-

##################################################################################
## Company: 
## Engineer: Oziel da Silva
## 
## Create Date: 02-09-2017 10:40 AM
## Module Name:Interpolação de imagem  
## Description: interpolação de imagens usando o método de vizinhos mais próximos
## Additional Comments:
## 
##################################################################################
import cv2
import numpy as np
import matplotlib.pyplot as plt

lena_32 = cv2.imread("../img/lena_32.tif")
lena_64 = cv2.imread("../img/lena_64.tif")
lena_128= cv2.imread("../img/lena_128.tif")
lena_256 = cv2.imread("../img/lena_256.tif")

woman_32 = cv2.imread("../img/woman_32.tif")
woman_64 = cv2.imread("../img/woman_64.tif")
woman_128 = cv2.imread("../img/woman_128.tif")
woman_256 = cv2.imread("../img/woman_256.tif")




interp_lena_32_512 = np.zeros(((512,512)), dtype= np.uint8)
interp_lena_64_512 = np.zeros(((512,512)), dtype= np.uint8)
interp_lena_128_512 = np.zeros(((512,512)), dtype= np.uint8)
interp_lena_256_512 = np.zeros(((512,512)), dtype= np.uint8)


fatorDeAmpliacao1 = 16
fatorDeAmpliacao2 = 8
fatorDeAmpliacao3 = 4
fatorDeAmpliacao4 = 2

for i in range(0, 32):
	for j in range(0, 32):
		interp_lena_32_512[(fatorDeAmpliacao1*i):(fatorDeAmpliacao1*(i+1)),(fatorDeAmpliacao1*j):(fatorDeAmpliacao1*(j+1))] = lena_32[i][j][1]

for i in range(0, 64):
	for j in range(0, 64):
		interp_lena_64_512[(fatorDeAmpliacao2*i):(fatorDeAmpliacao2*(i+1)),(fatorDeAmpliacao2*j):(fatorDeAmpliacao2*(j+1))] = lena_64[i][j][1]

for i in range(0, 128):
	for j in range(0, 128):
		interp_lena_128_512[(fatorDeAmpliacao3*i):(fatorDeAmpliacao3*(i+1)),(fatorDeAmpliacao3*j):(fatorDeAmpliacao3*(j+1))] = lena_128[i][j][1]

for i in range(0, 256):
	for j in range(0, 256):
		interp_lena_256_512[(fatorDeAmpliacao4*i):(fatorDeAmpliacao4*(i+1)),(fatorDeAmpliacao4*j):(fatorDeAmpliacao4*(j+1))] = lena_256[i][j][1]

cv2.imwrite('../img/interp_VIZINHO_32_512_lena.tif', interp_lena_32_512)
cv2.imwrite('../img/interp_VIZINHO_64_512_lena.tif', interp_lena_64_512)
cv2.imwrite('../img/interp_VIZINHO_128_512_lena.tif', interp_lena_128_512)
cv2.imwrite('../img/interp_VIZINHO_256_512_lena.tif', interp_lena_256_512)

plt.subplot(221)
plt.imshow(interp_lena_32_512,cmap = "gray")
plt.subplot(222)
plt.imshow(interp_lena_64_512, cmap = "gray")
plt.subplot(223)
plt.imshow(interp_lena_128_512, cmap = "gray")
plt.subplot(224)
plt.imshow(interp_lena_256_512, cmap = "gray")
plt.show()

