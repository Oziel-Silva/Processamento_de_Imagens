close all;
clear all;
clc;

imagem1 = imread('lena_gray_512.tif');
imagem2 = imread('jetplane.tif');
%FID = fopen('imagemSaida','w+');



fatorDeReducao = 1/16;

tamanhoHorizontal=(length(imagem1(1,:))*fatorDeReducao); %Largura da imagem
tamanhoVertical=(length(imagem1(:,1))*fatorDeReducao); %Altura da imagem

    for j=1:tamanhoHorizontal %Linhas horizontais

        for i=1:tamanhoVertical %Linhas verticais

             resImagem1(i,j)=imagem1((i/fatorDeReducao),(j/fatorDeReducao));

        end

    end


imwrite(resImagem1,'imagemSaida.tif');
imshow(resImagem1)