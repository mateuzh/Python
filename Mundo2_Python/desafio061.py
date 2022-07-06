#código para calcular do 1º ao 10º termo de uma pa utilizando o laço while

print('Calculando a PA!')
print('=-'*15)

t1 = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
cont = 1
while cont < 11:
    print(t1, end='')
    print(' -> ' if cont < 10 else ' ', end='')
    cont += 1
    t1 += razao


