import cv2
import matplotlib.pyplot as plt
import numpy as np

im1 = cv2.imread("lena_gray_512.tif")
print( im1.shape)

reducao = 1/2

nova_imagem = np.zeros((256,256))

for  i in range(0, 256):
    for j in range(0, 256):
        nova_imagem[i,j] = im1[int(i/reducao), int(j/reducao),1]

plt.subplot(211)
plt.imshow(im1)
plt.subplot(212)
plt.imshow(nova_imagem, cmap = "gray")
plt.show()