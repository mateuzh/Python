#código para achar o menor e maior valor dentre 3 valores digitados.

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
n3 = int(input('Digite o terceiro valor: '))
if n1 > n2 and n3:
    maiorvalor=n1
if n2 > n1 and n3:
    maiorvalor=n2
if n3 > n1 and n2:
    maiorvalor=n3
if n1 < n2 and n3:
    menorvalor=n1
if n2 < n1 and n3:
    menorvalor=n2
if n3 < n1 and n2:
    menorvalor=n3
print(f'O maior valor foi \033[42m{maiorvalor}\033[m')
print(f'O menor valor foi \033[43m{menorvalor}\033[m')