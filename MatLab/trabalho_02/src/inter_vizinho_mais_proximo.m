%interpolção por vizinho mais próximo

clear all;
close all;
clc;

imagem1 = imread('imagemSaida.tif');
%imagem2 = zeros(512,512,'uint8');
tamanho = length(imagem1);
fatorDeAmpliacao = 16;
k =1;
m =1;

for i=0 : (length(imagem1)-1)
    for j=0:(length(imagem1)-1)
        
        imagem2((1+fatorDeAmpliacao*i):fatorDeAmpliacao*(i+1),(1+fatorDeAmpliacao*j):fatorDeAmpliacao*(j+1)) = imagem1(i+1,j+1);
        
      
    end
      
end

figure;
imshow(imagem1)
figure;
imshow(imagem2)