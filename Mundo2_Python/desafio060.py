'''from math import factorial
n = int(input('Digite um valor: '))
f = factorial(n)
print(f)''' #Cálculo de fatorial utilizando o módulo Factorial from math

'''n = int(input('Digite um valor: '))
c = n
f = 1
print(f'Calculando {n}! ', end='')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f)''' #Cálculo de fatorial utilizando o laço While

'''n = int(input('Digite um valor: '))
f = 1
print(f'Calculando {n}! = ', end='')
for c in range (n, 0, -1):
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
print(f)''' #Cálculo de fatorial utilizando o laço For