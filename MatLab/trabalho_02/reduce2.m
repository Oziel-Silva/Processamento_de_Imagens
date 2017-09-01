
razao_h=(length(A(1,:,1))*m); %Largura da imagem
razao_v=(length(A(:,1,1))*m); %Altura da imagem
for k=1:length(A(1,1,:))
 for j=1:razao_h %Linhas horizontais

 for i=1:razao_v %Linhas verticais

 B(i,j,k)=A((i/m),(j/m),k);

 end

 end

end 