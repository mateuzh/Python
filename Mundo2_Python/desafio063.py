print('Sequência de Fibonacci! ')
print('-='*15)
termos = int(input('Quantos termos você gostaria de mostrar? '))
n1 = 0
n2 = 1
n3 = 0
print(f'{n1} -> {n2} -> ', end='')
c = 2
while c < termos:
    c += 1
    n3 = n1 + n2
    print(n3, end=' ')
    print('-> ', end='')
    n1 = n2
    n2 = n3
print(f'FIM')