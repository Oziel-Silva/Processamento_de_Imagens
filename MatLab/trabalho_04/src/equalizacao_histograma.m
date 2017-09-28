close all;
clear all;
clc;

I = imread('../img/Fig0310(b)(washed_out_pollen_image).tif');
h = length (I);
w = length (I);
n = h*w;

[nk rk] = hist(double(I(:)), 0:255);
ps = nk/n;

for k = 1:length(ps)
    pk(k) = sum(ps(1:k));
end

for linha = 1:w
    for coluna = 1:h
        Io(linha,coluna) = round(255*pk(I(linha,coluna)+1));
    end
end

[nk2 rk2] = hist(double(Io(:)), 0:255);


subplot(2,2,1)
imshow(uint8(I));
title('Imagem Sem Equalização');

subplot(2,2,2)
plot(rk,nk);
title('Histograma');
axis([0 max(rk) 0 max(nk)]);

subplot(2,2,3)
imshow(uint8(Io));
title('Imagem com Equalização');

subplot(2,2,4)
plot(rk2, nk2);
title('Histograma');
axis([0 max(rk2) 0 max(nk2)]);