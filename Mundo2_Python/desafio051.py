#código para calcular do 1º ao 10º termo de uma pa utilizando o laço for

termo1 = int(input('Digite o primeiro termo: '))
razao = int(input('Digite qual é a razão: '))
for c in range(termo1, termo1+10*razao, razao):
    print(c, end=' -> ')
print('Acabou! ')
