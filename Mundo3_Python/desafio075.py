#Código para colocar mais de um valor na tupla com valores cedidos pelo usuário

soma = (int(input('Digite um valor: ')),
        int(input('Digite outro valor: ')),
        int(input('Digite mais um valor: ')),
        int(input('Digite o último valor: ')))

print(f'Os valores digitados foram: {soma}')
if 9 in soma:
    print(f'O número 9 apareceu: {soma.count(9)} vezes')
else:
    print(f'O valor 9 não foi digitado! ')
if 3 in soma:
    print(f'O número 3 apareceu na {soma.index(3)+1}ª posição! ')
else:
    print(f'O valor 3 não foi digitado em nenhuma posição! ')
print(f'Os números pares digitados foram: ', end='')
for par in soma:
    if par % 2 == 0:
        print(par, end=' ')
