#código para verificar se o valor digitado é um número primo

valor = int(input('Digite um valor: '))
s = 0
x = 0
for c in range(1, valor+1):
    if valor % c == 0:
        print('\033[32m', end=' ')
    else:
        print('\033[31m', end=' ')
    print(c, end=' ')
    s = valor % c
    if s == 0:
        x += 1
if x > 2 or x == 1:
    print(f'\n\033[31m O valor foi divisivel {x} vezes, então é numero NÃO PRIMO\033[m')
elif x == 2:
    print(f'\n\033[32mO valor foi divisivel {x} vezes, então é um numero PRIMO\033[m')
